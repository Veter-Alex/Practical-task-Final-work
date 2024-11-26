import React, { useState, useEffect } from "react";
import axios from "axios";

const Goodstable = () => {
    const [data, setData] = useState([]);
    const [categories, setCategories] = useState({});
    const [sellers, setSellers] = useState({});
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const goodsRequest = axios.get("http://127.0.0.1:8000/goods/");
                const categoriesRequest = axios.get("http://127.0.0.1:8000/categories/");
                const sellersRequest = axios.get("http://127.0.0.1:8000/sellers/");

                const [goodsResponse, categoriesResponse, sellersResponse] = await Promise.all([
                    goodsRequest, categoriesRequest, sellersRequest
                ]);

                setData(goodsResponse.data);
                setCategories(categoriesResponse.data.reduce((acc, category) => {
                    acc[category.id] = category.name;
                    return acc;
                }, {}));
                setSellers(sellersResponse.data.reduce((acc, seller) => {
                    acc[seller.id] = { name: seller.name, rating: seller.rating };
                    return acc;
                }, {}));
            } catch (error) {
                console.error(error);
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, []);

    return (
        <div className="goodstable-container">
            <h3>Товары:</h3>
            {loading ? (
                <p>Loading...</p>
            ) : (
                <table className="goodstable-table">
                    <thead>
                        <tr>
                            <th>Название</th>
                            <th>Цена</th>
                            <th>Стоимость доставки</th>
                            <th>Описание</th>
                            <th>Категория</th>
                            <th>Продавец</th>
                            <th>Рейтинг продавеца</th>
                        </tr>
                    </thead>
                    <tbody>
                        {data.map((item, index) => (
                            <tr key={index}>
                                <td>{item.name}</td>
                                <td>{item.price}</td>
                                <td>{item.shipping_price}</td>
                                <td>{item.description}</td>
                                <td>{categories[item.category]}</td>
                                <td>{sellers[item.seller]?.name}</td>
                                <td>{sellers[item.seller]?.rating}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            )}
        </div>
    );
};

export default Goodstable;
