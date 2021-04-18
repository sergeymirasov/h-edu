import styled from 'styled-components';

export const StyledNavigation = styled.nav`
  ul {
    list-style-type: none;
    display: flex;
    margin: 0;
    padding: 0;
  }

  li:not(:last-of-type) {
    margin-right: 16px;
  }

  a {
    font-size: 16px;
  }
`;
