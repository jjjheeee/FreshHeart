import * as React from 'react';
import { alpha, styled } from '@mui/material/styles';
import { Box } from '@/node_modules/@mui/material/index';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import Container from '@mui/material/Container';
import Divider from '@mui/material/Divider';
import MenuItem from '@mui/material/MenuItem';
import Drawer from '@mui/material/Drawer';
import MenuIcon from '@mui/icons-material/Menu';
import CloseRoundedIcon from '@mui/icons-material/CloseRounded';
import { SitemarkIcon } from '@/public/icons/CustomIcons';
import ColorModeIconDropdown from '../shared-theme/colorModelconDropdown';
import { useRouter } from 'next/navigation';
import type {} from '@mui/material/themeCssVarsAugmentation';
import { useSelector, useDispatch } from '@/node_modules/react-redux/dist/react-redux';
import { handleLogout } from '@/public/utils/functions';

export default function AppAppBar() {
  const dispatch = useDispatch();
  const router = useRouter();
  const [open, setOpen] = React.useState(false);

  const userInfo = useSelector((state: any) => state.user);

  const toggleDrawer = (newOpen: boolean) => () => {
    setOpen(newOpen);
  };

  return (
    <AppBar
      position="fixed"
      enableColorOnDark
      sx={{
        boxShadow: 0,
        bgcolor: 'transparent',
        backgroundImage: 'none',
        mt: 'calc(var(--template-frame-height, 0px) + 28px)',
      }}
    >
      <Container maxWidth="lg">
        <StyledToolbar variant="dense" disableGutters>
          <Box sx={{ flexGrow: 1, display: 'flex', alignItems: 'center', px: 0 }}>
            <SitemarkIcon />
            <Box sx={{ display: { xs: 'none', md: 'flex' } }}>
              <Button variant="text" color="info" size="small">
                Features
              </Button>
              <Button variant="text" color="info" size="small">
                Testimonials
              </Button>
              <Button variant="text" color="info" size="small">
                Highlights
              </Button>
              <Button variant="text" color="info" size="small">
                Pricing
              </Button>
              <Button variant="text" color="info" size="small" sx={{ minWidth: 0 }}>
                FAQ
              </Button>
              <Button variant="text" color="info" size="small" sx={{ minWidth: 0 }}>
                Blog
              </Button>
            </Box>
          </Box>
          <Box
            sx={{
              display: { xs: 'none', md: 'flex' },
              gap: 1,
              alignItems: 'center',
            }}
          >
            {userInfo.user.isLogin ? (
              <div>
                <Button onClick={() => router.push('/users/signin')} color="primary" variant="text" size="small">
                {userInfo.user.nickname}님
                </Button>
                <Button onClick={() => handleLogout(dispatch,true,router)} color="primary" variant="text" size="small">
                  logout
                </Button>
              </div>
            ) : (
              <div>
                <Button onClick={() => router.push('/users/signin')} color="primary" variant="text" size="small">
                  Sign in
                </Button>
                <Button onClick={() => router.push('/users/signup')} color="primary" variant="contained" size="small">
                  Sign up
                </Button>
              </div>
            )}
            <ColorModeIconDropdown />
          </Box>
          <Box sx={{ display: { xs: 'flex', md: 'none' }, gap: 1 }}>
            <ColorModeIconDropdown size="medium" />
            <IconButton aria-label="Menu button" onClick={toggleDrawer(true)}>
              <MenuIcon />
            </IconButton>
            <Drawer
              anchor="top"
              open={open}
              onClose={toggleDrawer(false)}
              PaperProps={{
                sx: {
                  top: 'var(--template-frame-height, 0px)',
                },
              }}
            >
              <Box sx={{ p: 2, backgroundColor: 'background.default' }}>
                <Box
                  sx={{
                    display: 'flex',
                    justifyContent: 'flex-end',
                  }}
                >
                  <IconButton onClick={toggleDrawer(false)}>
                    <CloseRoundedIcon />
                  </IconButton>
                </Box>
                <MenuItem>Features</MenuItem>
                <MenuItem>Testimonials</MenuItem>
                <MenuItem>Highlights</MenuItem>
                <MenuItem>Pricing</MenuItem>
                <MenuItem>FAQ</MenuItem>
                <MenuItem>Blog</MenuItem>
                <Divider sx={{ my: 3 }} />
                {userInfo.user.isLogin ? (
                  <div>
                    <MenuItem>
                      <Button onClick={() => router.push('/users/signin')} color="primary" variant="text" size="small">
                        {userInfo.user.nickname}님
                      </Button>
                    </MenuItem>
                    <MenuItem>
                      <Button onClick={() => handleLogout(dispatch,true,router)} color="primary" variant="text" size="small">
                        logout
                      </Button>
                    </MenuItem>
                  </div>
                ):(
                  <div>
                    <MenuItem>
                      <Button onClick={() => router.push('/users/signup')} color="primary" variant="contained" fullWidth>
                        Sign up
                      </Button>
                    </MenuItem>
                    <MenuItem>
                      <Button onClick={() => router.push('/users/signin')} color="primary" variant="outlined" fullWidth>
                        Sign in
                      </Button>
                    </MenuItem>
                  </div>
                )}
              </Box>
            </Drawer>
          </Box>
        </StyledToolbar>
      </Container>
    </AppBar>
  );
}

const StyledToolbar = styled(Toolbar)(({ theme }) => ({
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'space-between',
  flexShrink: 0,
  borderRadius: `calc(${theme.shape.borderRadius}px + 8px)`,
  backdropFilter: 'blur(24px)',
  border: '1px solid',
  borderColor: (theme.vars || theme).palette.divider,
  backgroundColor: theme.vars
    ? `rgba(${theme.vars.palette.background.defaultChannel} / 0.4)`
    : alpha(theme.palette.background.default, 0.4),
  boxShadow: (theme.vars || theme).shadows[1],
  padding: '8px 12px',
}));