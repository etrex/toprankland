#!/usr/bin/env node
/**
 * One-time migration: transform flat JSON schema → i18n schema
 * Run: node scripts/migrate-i18n.mjs
 */
import { readdir, readFile, writeFile } from 'fs/promises';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const dir = join(__dirname, '../src/content/rankings');

// Detect Chinese characters
function isChinese(text = '') {
  return /[\u4E00-\u9FFF\u3400-\u4DBF]/.test(text);
}

// Known zh-tw translations for current rankings
const titleZh = {
  'best-wireless-earbuds':     '最佳無線耳機 2026',
  'best-gaming-mice':          '最佳電競滑鼠 2026',
  'best-smart-watches':        '最佳智慧手錶 2026',
  'best-vpn-services':         '最佳 VPN 服務 2026',
  'best-mechanical-keyboards': '最佳機械鍵盤 2026',
  'best-ai-coding-assistants': '最佳 AI 程式輔助工具 2026',
};
const descZh = {
  'best-wireless-earbuds':     '每日更新的最佳真無線耳機排行榜，根據降噪、音質、通話品質、電池壽命和性價比綜合評分。',
  'best-gaming-mice':          '每日更新的最佳電競無線滑鼠排行榜，根據感測器性能、無線延遲、重量、做工品質和性價比評分。',
  'best-smart-watches':        '每日更新的最佳智慧手錶排行榜，根據健康追蹤、電池壽命、螢幕品質、應用生態和性價比評分。',
  'best-vpn-services':         '每日更新的最佳 VPN 服務排行榜，根據隱私保護、連線速度、伺服器數量、易用性和價格評分。',
  'best-mechanical-keyboards': '每日更新的最佳機械鍵盤排行榜，根據按鍵手感、做工品質、功能特性、輪詢率延遲和性價比評分。',
  'best-ai-coding-assistants': '每日更新的最佳 AI 程式輔助工具排行榜，根據程式碼品質、上下文理解、整合體驗、速度和性價比評分。',
};

const files = await readdir(dir);

for (const file of files.filter(f => f.endsWith('.json'))) {
  const data = JSON.parse(await readFile(join(dir, file), 'utf-8'));

  // Already migrated? (has i18n key at root)
  if (data.i18n) {
    console.log(`Skip (already migrated): ${file}`);
    continue;
  }

  const slug = data.slug;

  const migrated = {
    slug,
    category: data.category,
    scoreFactors: data.scoreFactors,

    i18n: {
      en: {
        title: data.title,
        description: data.description,
      },
      'zh-tw': {
        title: titleZh[slug] ?? data.title,
        description: descZh[slug] ?? data.description,
      },
    },

    competitors: (data.competitors ?? []).map(c => ({
      id: c.id,
      name: c.name,
      brand: c.brand,
      url: c.url,
      priceRange: c.priceRange,
      i18n: {
        en: { description: c.description ?? '' },
        'zh-tw': { description: '' }, // translator task will fill later
      },
    })),

    history: (data.history ?? []).map(entry => {
      const commentary = entry.commentary ?? '';
      const highlights = entry.highlights ?? [];
      const zh = isChinese(commentary);
      return {
        date: entry.date,
        rankings: entry.rankings,
        references: entry.references ?? [],
        i18n: {
          en: zh
            ? { commentary: '', highlights: [] }
            : { commentary, highlights },
          'zh-tw': zh
            ? { commentary, highlights }
            : { commentary: '', highlights: [] },
        },
      };
    }),
  };

  await writeFile(join(dir, file), JSON.stringify(migrated, null, 2) + '\n');
  console.log(`Migrated: ${file}`);
}

console.log('Done.');
