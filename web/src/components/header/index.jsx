import { Link } from 'react-router-dom';

import { Container } from '../container';
import { Navigation } from '../navigation';
import { StyledHeader } from './styles';

export const Header = () => {
  return (
    <StyledHeader>
      <Container>
        <Link to="/" style={{ display: 'block', marginRight: '145px' }}>
          PROF
        </Link>

        <Navigation />
      </Container>
    </StyledHeader>
  );
};
