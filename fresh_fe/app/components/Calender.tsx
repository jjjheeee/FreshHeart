import React, { useState } from 'react';
import { Box, Typography, Button, Grid } from '@mui/material';
import { Joy } from '@/public/icons/CustomIcons';


const daysOfWeek = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

const Calendar = () => {
  const [currentDate, setCurrentDate] = useState(new Date());

  // 현재 월의 시작일과 끝일 계산
  const startOfMonth = new Date(currentDate.getFullYear(), currentDate.getMonth(), 1);
  const endOfMonth = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 0);

  // 이전 월로 이동
  const prevMonth = () => {
    setCurrentDate(new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, 1));
  };

  // 다음 월로 이동
  const nextMonth = () => {
    setCurrentDate(new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 1));
  };

  // 날짜 생성
  const days = [];
  for (let i = 0; i < startOfMonth.getDay(); i++) {
    days.push(null); // 이전 달 빈칸
  }
  for (let i = 1; i <= endOfMonth.getDate(); i++) {
    days.push(i);
  }

  return (
    <Box
      sx={{
        border: '1px solid #ddd',
        borderRadius: '8px',
        overflow: 'hidden',
        fontFamily: 'Arial, sans-serif',
      }}
    >
      <Box
        sx={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          padding: '10px',
          backgroundColor: '#f5f5f5',
          borderBottom: '1px solid #ddd',
        }}
      >
        <Button onClick={prevMonth} sx={{ minWidth: 'unset' }}>
          &lt;
        </Button>
        <Typography variant="h6">
          {currentDate.toLocaleString('default', { month: 'long' })} {currentDate.getFullYear()}
        </Typography>
        <Button onClick={nextMonth} sx={{ minWidth: 'unset' }}>
          &gt;
        </Button>
      </Box>
      <Grid container sx={{ backgroundColor: '#f9f9f9', padding: '5px 0' }}>
        {daysOfWeek.map((day) => (
          <Grid item xs={1.71} key={day}>
            <Typography
              variant="subtitle2"
              sx={{
                textAlign: 'center',
                fontWeight: 'bold',
              }}
            >
              {day}
            </Typography>
          </Grid>
        ))}
      </Grid>
      <Grid container sx={{ padding: '5px' }}>
        {days.map((day, index) =>
          day ? (
            <Grid item xs={1.71} key={index}>
              <Box
                sx={{
                  textAlign: 'center',
                  padding: '30px',
                  backgroundColor: '#fff',
                  border: '1px solid #ddd',
                  borderRadius: '4px',
                  cursor: 'pointer',
                  '&:hover': {
                    backgroundColor: '#eee',
                  },
                }}
              >
                {day}<Joy/>
              </Box>
            </Grid>
          ) : (
            <Grid item xs={1.71} key={index} />
          )
        )}
      </Grid>
    </Box>
  );
}

export default Calendar;
