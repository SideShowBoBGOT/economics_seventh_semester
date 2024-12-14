# Параметри COCOMO II для проєкту cppfront

## Software Size (Розмір програмного забезпечення)
| Параметр | Значення | Обґрунтування |
|-----------|-------|---------------|
| SLOC | 39463 | Загальна кількість рядків коду в директоріях source та include |
| New Code | 100% | Експериментальний новий проєкт |
| Reused Code | 0% | Не застосовується - новий проєкт |
| Modified Code | 0% | Не застосовується - новий проєкт |
| Software Understanding | 30% | Середньо-високий, оскільки це компілятор C++ |
| Unfamiliarity | 0.6 | Високий, через експериментальний характер |

## Scale Drivers (Драйвери масштабу)
| Драйвер | Значення | Рейтинг | Обґрунтування |
|--------|-------|---------|---------------|
| Precedentedness | High | 3.72 | Існують подібні компілятори C++ |
| Architecture/Risk Resolution | High | 3.72 | Добре спроєктований Гербом Саттером |
| Team Cohesion | High | 3.72 | Досвідчена основна команда |
| Process Maturity | Nominal | 4.68 | Стандартна розробка з відкритим кодом |
| Development Flexibility | Nominal | 4.68 | Стандартна гнучкість |

## Cost Drivers - Product (Фактори вартості - Продукт)
| Фактор | Значення | Рейтинг | Обґрунтування |
|--------|-------|---------|---------------|
| Required Software Reliability | High | 1.15 | Критично для компілятора |
| Database Size | Low | 0.93 | Немає складних баз даних |
| Product Complexity | Very High | 1.30 | Складність компілятора |
| Developed for Reusability | High | 1.08 | Проєкт з відкритим кодом |
| Documentation Match | Nominal | 1.00 | Стандартна документація |

## Cost Drivers - Personnel (Фактори вартості - Персонал)
| Фактор | Значення | Рейтинг | Обґрунтування |
|--------|-------|---------|---------------|
| Analyst Capability | Very High | 0.71 | Досвідчена команда |
| Programmer Capability | Very High | 0.76 | Досвідчена команда |
| Personnel Continuity | Nominal | 1.00 | Природа відкритого коду |
| Application Experience | High | 0.88 | Експертиза в C++ |
| Platform Experience | Very High | 0.81 | Глибока експертиза |
| Language/Toolset Experience | Very High | 0.84 | Глибока експертиза |

## Cost Drivers - Platform (Фактори вартості - Платформа)
| Фактор | Значення | Рейтинг | Обґрунтування |
|--------|-------|---------|---------------|
| Time Constraint | Nominal | 1.00 | Немає жорстких термінів |
| Storage Constraint | Nominal | 1.00 | Стандартні обмеження |
| Platform Volatility | Nominal | 1.00 | Стандартна волатильність |

## Cost Drivers - Project (Фактори вартості - Проєкт)
| Фактор | Значення | Рейтинг | Обґрунтування |
|--------|-------|---------|---------------|
| Use of Software Tools | Very High | 0.78 | Сучасні інструменти |
| Multisite Development | High | 0.92 | Розподілена команда |
| Required Development Schedule | Nominal | 1.00 | Стандартний графік |

## Додаткові налаштування
| Параметр | Значення | Обґрунтування |
|-----------|-------|---------------|
| Maintenance Mode | Off | Оцінка початкової розробки |