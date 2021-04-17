import styled from 'styled-components';

import { br } from '../../utils/styles';

export const StyledContainer = styled.div`
  padding: 0 16px;

  ${br.md} {
    padding: 0 24px;
  }

  ${br.xl} {
    padding: 0 32px;
  }

  > .content {
    margin: 0 auto;
    max-width: ${({ maxWidth }) => maxWidth};
  }
`;
