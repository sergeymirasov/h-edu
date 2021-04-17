import { StyledFieldWrapper } from './styles';

export const FieldWrapper = ({ className, label, children }) => {
  return (
    <StyledFieldWrapper className={className}>
      <p>{label}</p>

      {children}
    </StyledFieldWrapper>
  );
};
