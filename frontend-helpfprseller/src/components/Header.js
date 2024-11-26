import React from "react";

const Header = () => {
    return (
        <header className="header-container">
            <h1>Система поддержки вывода товаров на рынок</h1>
            <nav className="header-nav">
                <ul>
                    <li>
                        <a href="/">Главная</a>
                    </li>
                    <li>
                        <a href="#">О системе</a>
                    </li>
                    <li>
                        <a href="#">Контакты</a>
                    </li>
                </ul>
            </nav>
        </header>
    );
};

export default Header;
