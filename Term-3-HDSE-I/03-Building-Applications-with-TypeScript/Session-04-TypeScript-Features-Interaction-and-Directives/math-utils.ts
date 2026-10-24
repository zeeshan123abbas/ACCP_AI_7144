// math-utils.ts - a module: anything "export"ed can be used by other files
export const PASS_MARK = 50;

export function percentage(obtained: number, total: number): number {
  return Math.round((obtained / total) * 100);
}
