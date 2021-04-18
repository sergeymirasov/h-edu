import styled from 'styled-components';

import { Container } from '../container';

export const StyledContainer = styled(Container)`
  > .content {
    min-height: calc(100vh - 60px);
    background-color: #fff;
    padding: 50px 0;
    display: flex;
    justify-content: center;
  }
`;

export const StyledContent = styled.div`
  width: ${({ width }) => width || '100%'};

  > h1 {
    font-weight: 500;
    font-size: 38px;
    line-height: 46px;
    margin-bottom: 45px;
  }
`;
