import React from 'react';
import { useTranslation } from 'react-i18next';

const CropsFruits = () => {
    const { t } = useTranslation();

    const seasons = [
        {
            name: t('season.kharif', 'Kharif (Monsoon)'),
            period: 'June - October',
            description: 'Crops sown at the beginning of the rainy season.',
            crops: [
                { name: 'Rice (Paddy)', image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Rice_plants_at_sunrise.jpg/640px-Rice_plants_at_sunrise.jpg' },
                { name: 'Maize', image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Corn_field_in_summer.jpg/640px-Corn_field_in_summer.jpg' },
                { name: 'Cotton', image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Cotton_plant.jpg/640px-Cotton_plant.jpg' },
                { name: 'Sugarcane', image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sugarcane_field.jpg/640px-Sugarcane_field.jpg' },
                { name: 'Soybean', image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Soybean_field.jpg/640px-Soybean_field.jpg' },
                { name: 'Groundnut', image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Peanut_field.jpg/640px-Peanut_field.jpg' }
            ]
        },
        {
            name: t('season.rabi', 'Rabi (Winter)'),
            period: 'October - March',
            description: 'Crops sown in winter and harvested in spring.',
            crops: [
                { name: 'Wheat', image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Wheat_field_in_Ukraine.jpg/640px-Wheat_field_in_Ukraine.jpg' },
                { name: 'Barley', image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Barley_field.jpg/640px-Barley_field.jpg' },
                { name: 'Gram (Chickpea)', image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Chickpea_field.jpg/640px-Chickpea_field.jpg' },
                { name: 'Mustard', image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Mustard_field.jpg/640px-Mustard_field.jpg' },
                { name: 'Peas', image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Pea_plant.jpg/640px-Pea_plant.jpg' },
                { name: 'Potato', image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Potato_plant.jpg/640px-Potato_plant.jpg' }
            ]
        },
        {
            name: t('season.zaid', 'Zaid (Summer)'),
            period: 'March - June',
            description: 'Short season crops grown between Rabi and Kharif.',
            crops: [
                { name: 'Watermelon', image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Watermelon_field.jpg/640px-Watermelon_field.jpg' },
                { name: 'Muskmelon', image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Muskmelon.jpg/640px-Muskmelon.jpg' },
                { name: 'Cucumber', image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Cucumber_plant.jpg/640px-Cucumber_plant.jpg' },
                { name: 'Bitter Gourd', image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Bitter_gourd_plant.jpg/640px-Bitter_gourd_plant.jpg' },
                { name: 'Pumpkin', image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Pumpkin_plant.jpg/640px-Pumpkin_plant.jpg' }
            ]
        },
        {
            name: t('season.year_round', 'Year-Round / Perennial'),
            period: 'All Year',
            description: 'Fruits and crops that grow throughout the year.',
            crops: [
                { name: 'Banana', image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Banana_tree.jpg/640px-Banana_tree.jpg' },
                { name: 'Coconut', image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Coconut_tree.jpg/640px-Coconut_tree.jpg' },
                { name: 'Papaya', image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Papaya_tree.jpg/640px-Papaya_tree.jpg' },
                { name: 'Lemon', image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Lemon_tree.jpg/640px-Lemon_tree.jpg' },
                { name: 'Mango', image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Mango_tree.jpg/640px-Mango_tree.jpg' }
            ]
        }
    ];

    return (
        <div className="min-h-screen bg-gray-50 pt-24 pb-12 px-4 sm:px-6 lg:px-8">
            <div className="max-w-7xl mx-auto">
                <div className="text-center mb-12">
                    <h1 className="text-4xl font-extrabold text-green-900 mb-4 tracking-tight">
                        {t('crops.title', 'Seasonal Crops & Fruits Guide')}
                    </h1>
                    <p className="text-xl text-gray-600 max-w-2xl mx-auto">
                        {t('crops.subtitle', 'Explore a comprehensive list of crops suitable for different seasons to maximize your farm\'s productivity.')}
                    </p>
                </div>

                {seasons.map((season, index) => (
                    <div key={index} className="mb-16">
                        <div className="flex items-center mb-6">
                            <div className="bg-green-600 w-1.5 h-10 mr-4 rounded-full"></div>
                            <div>
                                <h2 className="text-2xl font-bold text-gray-800">{season.name}</h2>
                                <div className="flex items-center text-sm text-gray-500 mt-1">
                                    <span className="bg-green-100 text-green-800 px-2 py-0.5 rounded mr-2 font-medium">{season.period}</span>
                                    <span>{season.description}</span>
                                </div>
                            </div>
                        </div>

                        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
                            {season.crops.map((crop, idx) => (
                                <div key={idx} className="bg-white rounded-xl shadow-md overflow-hidden hover:shadow-xl transition-shadow duration-300 transform hover:-translate-y-1">
                                    <div className="h-48 overflow-hidden relative group">
                                        <img
                                            src={crop.image}
                                            alt={crop.name}
                                            className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
                                            onError={(e) => { e.target.src = 'https://placehold.co/600x400?text=No+Image'; }}
                                        />
                                        <div className="absolute inset-0 bg-black bg-opacity-20 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                                    </div>
                                    <div className="p-4 bg-white border-t border-gray-100">
                                        <h3 className="font-bold text-lg text-gray-800">{crop.name}</h3>
                                        <button className="mt-3 w-full bg-green-50 text-green-700 py-2 rounded-lg text-sm font-medium hover:bg-green-100 transition-colors">
                                            {t('view_details', 'View Details')}
                                        </button>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default CropsFruits;
