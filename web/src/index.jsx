import { render } from 'react-dom';

import { App } from './modules/app';
import './index.css';

const app = <App />;
const root = document.getElementById('root');

render(app, root);
