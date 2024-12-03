"use client"
import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Container from '@mui/material/Container';
import AppAppBar from './components/AppAppBar';
import MainContent from './components/MainContent';
import Latest from './components/Latest';
import Footer from './components/Footer';
import AppTheme from './shared-theme/AppTheme';

const BlogContent = ({ disableCustomTheme }: { disableCustomTheme?: boolean }) => {
  return (
    <AppTheme disableCustomTheme={disableCustomTheme}>
      <CssBaseline enableColorScheme />
      <AppAppBar />
      <Container
        maxWidth="lg"
        component="main"
        sx={{ display: 'flex', flexDirection: 'column', my: 16, gap: 4 }}
      >
        <Latest />
        <MainContent />
        <Footer />
      </Container>
    </AppTheme>
  );
};

export default function Blog() {
  return <BlogContent />;
}