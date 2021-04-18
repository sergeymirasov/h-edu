import { Link } from 'react-router-dom';

import { StyledNavigation } from './styles';

const list = [
  {
    title: 'Мои отчеты',
    path: '/reports',
  },
];

export const Navigation = () => {
  return (
    <StyledNavigation>
      <ul>
        {list.map(({ title, path }) => (
          <li>
            <Link to={path}>{title}</Link>
          </li>
        ))}
      </ul>
    </StyledNavigation>
  );
};
