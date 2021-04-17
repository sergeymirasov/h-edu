import styled from 'styled-components';

export const StyledPage = styled.div`
  min-height: 100vh;
  background-color: #fff;
  padding: 45px 0;

  .dynamic-field {
    display: flex;

    & > div {
      width: 100%;
    }
  }

  .dynamic-delete-button {
    position: relative;
    top: 4px;
    margin: 0 8px;
    color: #999;
    font-size: 24px;
    cursor: pointer;
    transition: all 0.3s;
  }

  .dynamic-delete-button:hover {
    color: #777;
  }

  .dynamic-delete-button[disabled] {
    cursor: not-allowed;
    opacity: 0.5;
  }
`;

export const AccentWrapper = styled.div`
  background-color: #f3f6f8;
  padding: 24px 24px 0;
  margin: 16px 0 40px;
`;
