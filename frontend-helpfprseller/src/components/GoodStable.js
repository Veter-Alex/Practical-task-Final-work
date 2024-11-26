import React, { useState, useEffect } from "react";
import axios from "axios";

const Goodstable = () => {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [selectedCategory, setSelectedCategory] = useState(null);
    const [selectedGood, setSelectedGood] = useState(null);

    useEffect(() => {
        axios
            .get("http://127.0.0.1:8000/goods/")
            .then((response) => {
                setData(response.data);
                setLoading(false);
            })
            .catch((error) => {
                console.error(error);
            });
    }, []);

    const handleUpdateData = (newData) => {
        setData(newData);
    };

    return (
        <div className="goodstable-container">
            <p>Товары из Китая:</p>
            <table className="goodstable-table">
                <thead>
                    <tr>
                        <th>Картинка</th>
                        <th>Имя</th>
                        <th>Цена</th>
                        <th>Стоимость доставки</th>
                        <th>Описание</th>
                        <th>Категория</th>
                        <th>Продавец</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map((item, index) => (
                        <tr key={index} >
                            <td>{item.image}</td>
                            <td>{item.name}</td>
                            <td>{item.price}</td>
                            <td>{item.shipping_price}</td>
                            <td>{item.description}</td>
                            <td>{item.category}</td>
                            <td>{item.seller}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Goodstable;
