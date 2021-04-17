import React from 'react';

import { StyledContainer } from './styles';

export const Container = ({ className, children, maxWidth = '1400px' }) => {
  return (
    <StyledContainer className={className} maxWidth={maxWidth}>
      <div className="content">{children}</div>
    </StyledContainer>
  );
};
