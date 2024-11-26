import React, { useEffect, useState } from "react";
import axios from "axios";

const MenuGoodstable = () => {
    const [categories, setCategories] = useState([]);
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
    }, []);

    const handleCategoryClick = (categoryId) => {
        setSelectedCategory(categoryId);
        axios
            .get(`http://127.0.0.1:8000/goods/categories/${categoryId}`)
            .then((response) => {
                console.log({categoryId});
                console.log(response.data);
                setCategories(response.data);
            })
            .catch((error) => {
                console.error(error);
            });
    };

    return (
        <nav className="menu-goodstable">
            <ul>
                {categories.map((category) => (
                    <li key={category.id}>
                        <a
                            href={`#`}
                            onClick={() => handleCategoryClick(category.id)}
                        >
                            {category.name}
                        </a>
                    </li>
                ))}
            </ul>
        </nav>
    );
};

export default MenuGoodstable;
