import React, { useEffect, useState } from "react";
import axios from "axios";

const MenuGoodstable = () => {
    const [categories, setCategories] = useState([]);
    const [sellers, setSellers] = useState([]);
    const [selectedCategory, setSelectedCategory] = useState(null);

    useEffect(() => {
        // Выполняем запрос к API для получения категорий
        axios
            .get("http://127.0.0.1:8000/categories/")
            .then((response) => {
                setCategories(response.data);
            })
            .catch((error) => {
                console.error(error);
            });
        axios
            .get("http://127.0.0.1:8000/sellers/")
            .then((response) => {
                setSellers(response.data);
            })
            .catch((error) => {
                console.error(error);
            });
    }, []);

    return (
        <nav className="menu-goodstable">
            <h3>Категории:</h3>
            <ul>
                <li>
                    <a href={`#`}>Все категории</a>
                </li>
                {categories.map((category) => (
                    <li key={category.id}>
                        <a href={`#`}>{category.name}</a>
                    </li>
                ))}
            </ul>
            <h3>Продавцы:</h3>
            <ul>
                <li>
                    <a href={`#`}>Все продавцы</a>
                </li>
                {sellers.map((seller) => (
                    <li key={seller.id}>
                        <a href={`#`}>{seller.name}</a>
                    </li>
                ))}
            </ul>
        </nav>
    );
};

export default MenuGoodstable;
