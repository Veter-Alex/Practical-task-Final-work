import React, { useState, useEffect } from "react";

const ProfitCalculator = () => {
    const [goodPrice, setGoodPrice] = useState(0); // стоимость товара
    const [deliveryCost, setDeliveryCost] = useState(0); // стоимость доставки
    const [customsCost, setCustomsCost] = useState(0); // стоимость растаможки
    const [finalGoodCost, setFinalGoodCost] = useState(0); // итоговая стоимость после доставки и растаможки
    const [markingCost, setMarkingCost] = useState(0); // стоимость маркировки
    const [packagingCost, setPackagingCost] = useState(0); // стоимость упаковки
    const [otherAdditionalCost, setOtherAdditionalCost] = useState(0); // другие затраты на подготовку
    const [finalAdditionalCost, setFinalAdditionalCost] = useState(0); // итоговые затраты на подготовку
    const [commissionTradingPlatform, setCommissionTradingPlatform] =
        useState(0); // комиссия торговой площадки
    const [otherTradingPlatformCosts, setOtherTradingPlatformCosts] =
        useState(0); // другие затраты на торговую площадку
    const [finalTradingPlatformCosts, setFinalTradingPlatformCosts] =
        useState(0); // итоговые затраты на торговую площадку
    const [ownPrice, setOwnPrice] = useState(0); // собственная цена
    const [netProfit, setNetProfit] = useState(0); // чистая прибыль
    const [profit, setProfit] = useState(0); // рентабельность товара

    useEffect(() => {
        calculateProfit();
    }, [
        goodPrice, // цена товара
        deliveryCost, // стоимость доставки
        customsCost, // стоимость растаможки
        finalGoodCost, // итоговая стоимость товара после доставки и растаможки
        markingCost, // стоимость маркировки
        packagingCost, // стоимость упаковки
        otherAdditionalCost, // другие затраты на подготовку
        finalAdditionalCost, // итоговые затраты на подготовку
        commissionTradingPlatform, // комиссия торговой площадки
        otherTradingPlatformCosts, // другие затраты на торговую площадку
        finalTradingPlatformCosts, // итоговые затраты на торговую площадку
        ownPrice, // собственная цена
    ]);

    const calculateProfit = () => {
        const finalGoodCost =
            parseFloat(goodPrice) +
            parseFloat(deliveryCost) +
            parseFloat(customsCost);
        setFinalGoodCost(finalGoodCost); // итоговая стоимость товара после доставки и растаможки

        const finalAdditionalCost =
            parseFloat(markingCost) +
            parseFloat(packagingCost) +
            parseFloat(otherAdditionalCost);
        setFinalAdditionalCost(finalAdditionalCost); // итоговые затраты на подготовку

        const finalTradingPlatformCosts =
            (parseFloat(ownPrice) / 100 * parseFloat(commissionTradingPlatform) +
            parseFloat(otherTradingPlatformCosts)).toFixed(2);
        setFinalTradingPlatformCosts(finalTradingPlatformCosts); // итоговые затраты на торговую площадку

        // итоговая стоимость со всеми затратами
        const totalCost =
            parseFloat(finalGoodCost) +
            parseFloat(finalAdditionalCost) +
            parseFloat(finalTradingPlatformCosts);
        // чистая прибыль
        const netProfit = (parseFloat(ownPrice) - parseFloat(totalCost)).toFixed(2);
        setNetProfit(netProfit);
        // рентабельность
        const profit = ((parseFloat(netProfit) / parseFloat(ownPrice)) * 100).toFixed(2);;
        if (profit === "NaN") {
            setProfit(0);
        }
        else if (profit < 0)
            setProfit(0);
        else
            setProfit(profit);
    };


    const handleInputChange = (event) => {
        const { name, value } = event.target;
        switch (name) {
            case "goodPrice":
                setGoodPrice(value);
                break;
            case "deliveryCost":
                setDeliveryCost(value);
                break;
            case "customsCost":
                setCustomsCost(value);
                break;
            case "markingCost":
                setMarkingCost(value);
                break;
            case "packagingCost":
                setPackagingCost(value);
                break;
            case "otherAdditionalCost":
                setOtherAdditionalCost(value);
                break;
            case "commissionTradingPlatform":
                setCommissionTradingPlatform(value);
                break;
            case "otherTradingPlatformCosts":
                setOtherTradingPlatformCosts(value);
                break;
            case "ownPrice":
                setOwnPrice(value);
                break;
            case "netProfit":
                setNetProfit(value);
                break;
            default:
                break;
        }
    };
    
    return (
        <div>
            <h3>Расчет рентабельности вывода товара на рынок:</h3>
            <form className="profit-calculator-form">
                <div className="good-cost">
                    <p>Информация о товаре:</p>
                    <div className="good-cost-fields">
                        <label>
                            Цена товара:
                            <input
                                type="number"
                                name="goodPrice"
                                value={goodPrice}
                                onChange={handleInputChange}
                            />
                        </label>
                        <label>
                            Стоимость доставки:
                            <input
                                type="number"
                                name="deliveryCost"
                                value={deliveryCost}
                                onChange={handleInputChange}
                            />
                        </label>
                        <label>
                            Стоимость таможенной пошлины:
                            <input
                                type="number"
                                name="customsCost"
                                value={customsCost}
                                onChange={handleInputChange}
                            />
                        </label>
                    </div>
                    <label className="final-good-cost intermediate-values">
                        Стоимость товара после доставки и уплаты таможенной
                        пошлины: {finalGoodCost}
                    </label>
                </div>

                <div className="additional-cost">
                    <p>Подготовительные расходы:</p>
                    <div className="additional-cost-fields">
                        <label>
                            Стоимость маркировки:
                            <input
                                type="number"
                                name="markingCost"
                                value={markingCost}
                                onChange={handleInputChange}
                            />
                        </label>
                        <label>
                            Стоимость упаковки:
                            <input
                                type="number"
                                name="packagingCost"
                                value={packagingCost}
                                onChange={handleInputChange}
                            />
                        </label>
                        <label>
                            Прочие подготовительные расходы:
                            <input
                                type="number"
                                name="otherAdditionalCost"
                                value={otherAdditionalCost}
                                onChange={handleInputChange}
                            />
                        </label>
                    </div>
                    <label className="final-additional-cost intermediate-values">
                        Итоговые подготовительные расходы: {finalAdditionalCost}
                    </label>
                </div>

                <div className="trading-platform-cost">
                    <p>Расходы торговой площадки:</p>
                    <div className="trading-platform-cost-fields">
                        <label>
                            Комиссия торговой площадки:
                            <input
                                type="number"
                                name="commissionTradingPlatform"
                                value={commissionTradingPlatform}
                                onChange={handleInputChange}
                            />%
                        </label>
                        <label>
                            Прочие расходы торговой площадки:
                            <input
                                type="number"
                                name="otherTradingPlatformCosts"
                                value={otherTradingPlatformCosts}
                                onChange={handleInputChange}
                            />
                        </label>
                    </div>
                    <label className="final-trading-platform-cost intermediate-values">
                        Итоговые расходы торговой площадки:{" "}
                        {finalTradingPlatformCosts}
                    </label>
                </div>

                <div className="profit">
                    <p>Расчет прибыли и рентабельности:</p>
                    <div className="profit-fields">
                        <label>
                            Планируемая цена продажи:
                            <input
                                type="number"
                                name="ownPrice"
                                value={ownPrice}
                                onChange={handleInputChange}
                            />
                        </label>
                    </div>
                    <label className="net-profit-intermediate-values">
                        Чистая прибыль: {netProfit}
                    </label>
                    <p></p>
                    <label className="profit-intermediate-values">
                        Рентабельность продажи товара: {profit} %
                    </label>
                </div>
            </form>
        </div>
    );
};

export default ProfitCalculator;
