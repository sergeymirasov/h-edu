import { createElement } from 'react';

const sizes = {
  large: {
    tag: 'h1',
    style: {
      fontSize: '38px',
      lineHeight: '46px',
      margin: '0 0 60px',
      fontWeight: 500,
    },
  },
  medium: {
    tag: 'h2',
    style: {
      fontSize: '30px',
      lineHeight: '38px',
      margin: '0 0 32px',
      fontWeight: 500,
    },
  },
  small: {
    tag: 'h3',
    style: {
      fontSize: '20px',
      lineHeight: '28px',
      margin: '0 0 24px',
      fontWeight: 500,
    },
  },
};

export const ContentTitle = ({ size, children, className }) => {
  const { tag, style } = sizes[size];

  return createElement(tag, {
    style,
    className,
    children,
  });
};
