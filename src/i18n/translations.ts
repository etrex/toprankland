export const supportedLangs = ['en', 'zh-tw'] as const;
export type Lang = typeof supportedLangs[number];
export const defaultLang: Lang = 'en';

export const langNames: Record<Lang, string> = {
  'en': 'English',
  'zh-tw': '繁體中文',
};

export const ui = {
  en: {
    site_tagline: 'Curated Rankings for Everything',
    nav_all_rankings: 'All Rankings',
    hero_subtitle: "Carefully curated rankings, tracked daily. See what's rising, what's falling, and why.",
    movers_title: "Today's Biggest Movers",
    all_categories: 'All',
    entries_updated: 'entries · updated daily',
    rank_trend: 'Rank Trend — Top 10',
    chart_note_pre: 'Lower = better rank. Showing last',
    chart_note_post: 'days.',
    current_rankings: 'Current Rankings',
    todays_analysis: "Today's Analysis",
    key_highlights: 'Key Highlights',
    references: 'References',
    update_history: 'Update History',
    last_updated: 'Last updated',
    entries_tracked: 'entries tracked daily',
    back_all: '← All Rankings',
    footer: 'Curated Rankings for Everything',
  },
  'zh-tw': {
    site_tagline: '精選排行榜，每日追蹤',
    nav_all_rankings: '所有排行榜',
    hero_subtitle: '精心策劃的排行榜，每日追蹤。看看什麼在上升、什麼在下跌，以及原因。',
    movers_title: '今日最大變動',
    all_categories: '全部',
    entries_updated: '項目 · 每日更新',
    rank_trend: '排名走勢 — 前 10 名',
    chart_note_pre: '數字越小代表排名越高。顯示最近',
    chart_note_post: '天。',
    current_rankings: '當前排名',
    todays_analysis: '今日分析',
    key_highlights: '重點摘要',
    references: '參考資料',
    update_history: '更新歷史',
    last_updated: '最後更新',
    entries_tracked: '項目每日追蹤',
    back_all: '← 所有排行榜',
    footer: '精選排行榜，每日追蹤',
  },
} as const;

export function useTranslations(lang: Lang) {
  return function t(key: keyof typeof ui['en']): string {
    return (ui[lang] as Record<string, string>)[key] ?? ui[defaultLang][key];
  };
}

/** Check if an i18n value has meaningful content (non-empty string, non-empty array, non-empty object) */
function hasContent(val: any): boolean {
  if (!val) return false;
  if (typeof val === 'string') return val.length > 0;
  if (Array.isArray(val)) return val.length > 0;
  if (typeof val === 'object') return Object.values(val).some(v => hasContent(v));
  return Boolean(val);
}

/**
 * Get i18n content with smart fallback.
 * Falls back to other languages if the preferred lang value is empty/missing.
 * preferred lang → EN → zh-tw
 */
export function getI18n(obj: Record<string, any> | undefined, lang: Lang): any {
  if (!obj) return undefined;
  const preferred = obj[lang];
  if (hasContent(preferred)) return preferred;
  const fallbacks: string[] = lang !== defaultLang ? [defaultLang, 'zh-tw'] : ['zh-tw'];
  for (const fb of fallbacks) {
    if (fb !== lang && hasContent(obj[fb])) return obj[fb];
  }
  return preferred; // return even if empty, better than undefined
}
