export const sizes = {
  sm: 576,
  md: 768,
  lg: 992,
  xl: 1200,
};

export const queries = {
  sm: `screen and (min-width: ${sizes.sm}px)`,
  md: `screen and (min-width: ${sizes.md}px)`,
  lg: `screen and (min-width: ${sizes.lg}px)`,
  xl: `screen and (min-width: ${sizes.xl}px)`,
};

export const br = {
  sm: `@media ${queries.sm}`,
  md: `@media ${queries.md}`,
  lg: `@media ${queries.lg}`,
  xl: `@media ${queries.xl}`,
};
