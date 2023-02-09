import * as React from 'react';
import Box from '@mui/material/Box';
import BottomNavigation from '@mui/material/BottomNavigation';
import BottomNavigationAction from '@mui/material/BottomNavigationAction';
import RestoreIcon from '@mui/icons-material/Restore';
import FavoriteIcon from '@mui/icons-material/Favorite';
import LocationOnIcon from '@mui/icons-material/LocationOn';
import { Link } from "react-router-dom"

export default function Navigation(){
  const [value, setValue] = React.useState(0);

  return (
    <Box sx={{ width: 500 }}>
      <BottomNavigation
        value={value}
        onChange={(event, newValue) => {
          setValue(newValue);
        }}
      >
        <Link to="/home" style={{width:50, margin:10}}>홈</Link>
        <Link to="/todos" style={{width:50, margin:10}}>할일</Link>
        <Link to="/signup" style={{width:50, margin:10}}>회원가입</Link>
        <Link to="/login" style={{width:50, margin:10}}>로그인</Link>
        <Link to="/user-list" style={{width:50, margin:10}}>사용자목록</Link>
      </BottomNavigation>
    </Box>
  );
}