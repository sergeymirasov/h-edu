import { Button } from 'antd';
import { withRouter } from 'react-router-dom';

export const LinkButton = withRouter((props) => {
  const { history, location, match, staticContext, to, onClick, ...rest } = props;

  return (
    <Button
      {...rest}
      onClick={(event) => {
        onClick && onClick(event);
        history.push(to);
      }}
    />
  );
});
