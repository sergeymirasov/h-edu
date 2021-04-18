import { StyledContent, StyledContainer } from './styles';

export const PageContent = ({ children, title, width = '900px' }) => {
  return (
    <StyledContainer>
      <StyledContent width={width}>
        <h1>{title}</h1>

        {children}
      </StyledContent>
    </StyledContainer>
  );
};
