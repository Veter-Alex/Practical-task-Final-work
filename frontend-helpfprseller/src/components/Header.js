import React from "react";

const Header = () => {
    return (
        <header className="header-container">
            <h1>Аналитическая система расчета рентабельности вывода продукта на маркетплейс.</h1>
            <nav className="header-nav">
                <ul>
                    <li>
                        <a href="/">ГЛАВНАЯ</a>
                    </li>
                    <li>
                        <a href="#">О СИСТЕМЕ</a>
                    </li>
                    <li>
                        <a href="#">КОНТАКТЫ</a>
                    </li>
                </ul>
            </nav>
        </header>
    );
};

export default Header;
