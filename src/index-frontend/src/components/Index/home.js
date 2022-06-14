import React, { Component } from "react";
import MobileHome from './mobile-home'
import DesktopHome from './desktop-home'
import {useViewport} from '../../utils/viewport-provider'

const Home = () => {
    const { width } = useViewport();
    const breakpoint = 1000;
  
    return width < breakpoint ? <MobileHome /> : <DesktopHome />;
  };

export default Home;