// import logo from "./logo.svg";
import "./App.css";

import React from "react";
// import axios from "axios";

import Header from "./components/Header";
import MenuGoodstable from "./components/MenuGoodstable";
import Goodstable from "./components/GoodStable";
import ProfitCalculator from "./components/ProfitCalculator";
class App extends React.Component {
    render() {
        return (
            <div style={{ margin: "0", padding: "0" }}>
                <div className="header-container">
                    <Header />
                </div>
                <div className="main-container">
                    <MenuGoodstable />
                    <Goodstable />
                </div>
                <div className="footer-container">
                    <ProfitCalculator />
                </div>
            </div>
        );
    }
}

export default App;
