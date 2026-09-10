# -*- coding: utf-8 -*-
"""
知识库数据导出脚本
================
扫描所有 .md 文件 front matter，输出 CSV / JSON / Markdown 汇总表

用法：
    python scripts/export_data.py --format csv    # 输出到 exports/kb-index.csv
    python scripts/export_data.py --format json   # 输出到 exports/kb-index.json
    python scripts/export_data.py --format all    # 全部格式
"""

import glob
import re
import csv
import json
import os
import argparse
from datetime import datetime

CORE_PREFIXES = {'TH', 'CALC', 'PR', 'CASE'}

def parse_front_matter(content):
    """解析 YAML front matter（支持基础格式，不支持嵌套字典）"""
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).split('\n'):
        if ':' in line:
            key, _, val = line.partition(':')
            key = key.strip()
            val = val.strip()
            # 去掉引号
            val = val.strip('"').strip("'")
            fm[key] = val
    return fm

def scan_all():
    """扫描所有 md 文件，返回条目列表"""
    entries = []
    for md in glob.glob('docs/**/*.md', recursive=True):
        with open(md, 'r', encoding='utf-8') as f:
            content = f.read()
        fm = parse_front_matter(content)
        kb_id = fm.get('id', '')
        if not kb_id or '{' in kb_id:
            continue
        prefix = kb_id.split('-')[0]
        rel_path = md.replace('docs/', '')
        entries.append({
            'id': kb_id,
            'prefix': prefix,
            'title': fm.get('title', ''),
            'domain': fm.get('domain', ''),
            'status': fm.get('status', ''),
            'version': fm.get('version', ''),
            'updated': fm.get('updated', ''),
            'path': rel_path,
            'lines': len(content.split('\n')),
        })
    entries.sort(key=lambda x: x['id'])
    return entries

def export_csv(entries, out_path):
    """导出 CSV"""
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['id', 'prefix', 'title', 'domain', 'status', 'version', 'updated', 'lines', 'path'])
        w.writeheader()
        w.writerows(entries)

def export_json(entries, out_path):
    """导出 JSON"""
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    meta = {
        'generated_at': datetime.now().isoformat(),
        'total': len(entries),
        'by_prefix': {p: sum(1 for e in entries if e['prefix'] == p) for p in sorted(set(e['prefix'] for e in entries))},
        'entries': entries,
    }
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

def export_stats_md(entries, out_path):
    """导出 Markdown 统计页（供 README 引用）"""
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    lines = [
        '# 知识库条目统计（自动生成）',
        '',
        f'> 生成时间：{datetime.now().strftime("%Y-%m-%d %H:%M")} ｜ 条目总数：{len(entries)}',
        '',
        '## 按前缀分布',
        '',
        '| 前缀 | 层 | 数量 |',
        '|---|---|---|',
    ]
    cn = {'TH': '理论层', 'CALC': '计算层', 'PR': '实践层', 'CASE': '案例层',
          'CHG': '换版记录', 'EXAM': '考纲目录', 'REF': '中外对照', 'STD': '标准索引',
          'GOV': '治理文档', 'KB': '全站检索'}
    for pfx in sorted(set(e['prefix'] for e in entries)):
        cnt = sum(1 for e in entries if e['prefix'] == pfx)
        lines.append(f'| {pfx} | {cn.get(pfx, "-")} | {cnt} |')
    
    lines.extend([
        '',
        '## 四层核心明细',
        '',
        '| ID | 标题 | 状态 | 行数 |',
        '|---|---|---|---|',
    ])
    for e in entries:
        if e['prefix'] in CORE_PREFIXES:
            lines.append(f"| {e['id']} | {e['title']} | {e['status']} | {e['lines']} |")

    with open(out_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--format', choices=['csv', 'json', 'stats', 'all'], default='all')
    args = parser.parse_args()

    entries = scan_all()
    print(f'扫描到 {len(entries)} 个条目')

    out_dir = 'exports'

    if args.format in ('csv', 'all'):
        export_csv(entries, os.path.join(out_dir, 'kb-index.csv'))
        print(f'  ✅ CSV  → {out_dir}/kb-index.csv')

    if args.format in ('json', 'all'):
        export_json(entries, os.path.join(out_dir, 'kb-index.json'))
        print(f'  ✅ JSON → {out_dir}/kb-index.json')

    if args.format in ('stats', 'all'):
        export_stats_md(entries, os.path.join(out_dir, 'kb-stats.md'))
        print(f'  ✅ MD   → {out_dir}/kb-stats.md')

    # 汇总
    by_pfx = {}
    for e in entries:
        by_pfx.setdefault(e['prefix'], 0)
        by_pfx[e['prefix']] += 1
    print(f'\n📊 统计：TH={by_pfx.get("TH",0)} CALC={by_pfx.get("CALC",0)} PR={by_pfx.get("PR",0)} CASE={by_pfx.get("CASE",0)} 其他={sum(v for k,v in by_pfx.items() if k not in CORE_PREFIXES)}')

if __name__ == '__main__':
    main()
