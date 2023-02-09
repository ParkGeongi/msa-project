import * as React from 'react';
import Box from '@mui/material/Box';
import BottomNavigation from '@mui/material/BottomNavigation';

import { Link } from "react-router-dom"

const Navigation2 = () => {
  const [value, setValue] = React.useState(0);

  return (
    <Box sx={{ width: 'auto' }}>
      <BottomNavigation
        showLabels
        value={value}
        onChange={(newValue) => {
          setValue(newValue);
        }}
      >
        <Link to="/home" style={{width:'auto', margin: 10}}>Home</Link>
        <Link to="/counter" style={{width:'auto', margin:10}}>Counter</Link>
        <Link to="/todos" style={{width:'auto', margin:10}}>Todos</Link>


        <Link to="/stroke" style={{width:'auto', margin:10}}>Stroke</Link>
        <Link to="/iris" style={{width:'auto', margin:10}}>Iris</Link>
        <Link to="/fashion" style={{width:'auto', margin:10}}>Fashion</Link>
        <Link to="/number" style={{width:'auto', margin:10}}>Number</Link>
        <Link to="/navermoives" style={{width:'auto', margin:10}}>Naver_Movies</Link>
        <Link to="/samsung" style={{width:'auto', margin:10}}>Samsung</Link>
        <Link to="/sequsers" style={{width: 76, margin:10}}>Seq-Users</Link>
        <Link to="/review" style={{width:'auto', margin:10}}>Review</Link>
        <Link to="/sequserlist" style={{width:'auto', margin:10}}>SeqUserList</Link>
        <Link to="/seq-login" style={{width:'auto', margin:10}}>SeqLogin</Link>
        <Link to="/name" style={{width:'auto', margin:10}}>Name</Link>
        <Link to="/samsung-stock" style={{width:'auto', margin:10}}>Samsung_Stock</Link>
      </BottomNavigation>
    </Box>
  );
}

export default Navigation2