import styled from 'styled-components';

export const StyledHeader = styled.header`
  background-color: #141414;
  height: 60px;
  position: fixed;
  left: 0;
  right: 0;
  z-index: 1;

  .content {
    color: #fff;
    display: flex;
    align-items: center;
    height: 60px;
    font-weight: 500;
    font-size: 24px;
    line-height: 46px;
  }

  a {
    color: #fff;
  }
`;
