import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
    Sprout,
    Droplets,
    Sun,
    Wind,
    Cpu,
    Wifi,
    Smartphone,
    TrendingUp,
    ArrowRight,
    CheckCircle2,
    Calendar,
    Shovel,
    Recycle,
    Tractor
} from 'lucide-react';

const ModernFarming = () => {
    const [activeTab, setActiveTab] = useState('techniques');

    const fadeIn = {
        hidden: { opacity: 0, y: 20 },
        visible: { opacity: 1, y: 0 }
    };

    const techniques = [
        {
            title: "Vertical Farming",
            description: "Growing crops in vertically stacked layers, often incorporating controlled-environment agriculture.",
            icon: <Sprout className="w-8 h-8 text-green-400" />,
            benefits: ["95% less water usage", "Year-round crop production", "No pesticide requirement"],
            image: "https://images.unsplash.com/photo-1530836369250-ef72a3f5cda8?auto=format&fit=crop&q=80&w=1000"
        },
        {
            title: "Hydroponics",
            description: "A method of growing plants without soil, using mineral nutrient solutions in a water solvent.",
            icon: <Droplets className="w-8 h-8 text-blue-400" />,
            benefits: ["Faster growth rates", "Space efficient", "Higher yields"],
            image: "https://images.unsplash.com/photo-1556910103-1c02745a30bf?auto=format&fit=crop&q=80&w=1000"
        },
        {
            title: "Regenerative Ag",
            description: "Farming and grazing practices that reverse climate change by rebuilding soil organic matter.",
            icon: <Sun className="w-8 h-8 text-yellow-400" />,
            benefits: ["Carbon sequestration", "Improved soil health", "Biodiversity increase"],
            image: "https://images.unsplash.com/photo-1625246333195-78d9c38ad449?auto=format&fit=crop&q=80&w=1000"
        }
    ];

    const traditionalMethods = [
        {
            title: "Crop Rotation",
            description: "The practice of planting different crops sequentially on the same plot of land to improve soil health, optimize nutrients in the soil, and combat pest and weed pressure.",
            icon: <Recycle className="w-8 h-8 text-amber-500" />,
            benefits: ["Prevents soil depletion", "Controls pests naturally", "Reduces fertilizer dependency"],
            image: "https://images.unsplash.com/photo-1500651230702-0e2d8a49d4ad?auto=format&fit=crop&q=80&w=1000"
        },
        {
            title: "Organic Composting",
            description: "Recycling organic matter like leaves and food scraps into a valuable fertilizer that can enrich soil and plants.",
            icon: <Shovel className="w-8 h-8 text-emerald-600" />,
            benefits: ["Enriches soil nutrients", "Retains moisture", "Suppresses plant diseases"],
            image: "https://images.unsplash.com/photo-1585320806297-c798031c26b8?auto=format&fit=crop&q=80&w=1000"
        },
        {
            title: "Natural Pest Control",
            description: "Using biological methods (like beneficial insects) rather than chemicals to manage pest populations.",
            icon: <Sprout className="w-8 h-8 text-lime-500" />,
            benefits: ["Eco-friendly", "Safe for pollinators", "Cost-effective long term"],
            image: "https://images.unsplash.com/photo-1464226184884-fa280b87c399?auto=format&fit=crop&q=80&w=1000"
        }
    ];

    const tools = [
        {
            title: "Agricultural Drones",
            description: "UAVs used for precision monitoring, mapping, and spraying crops.",
            icon: <Wind className="w-12 h-12 mb-4 text-sky-400" />,
            stats: "30% Cost Reduction"
        },
        {
            title: "IoT Sensors",
            description: "Smart sensors for real-time monitoring of soil moisture, temperature, and acidity.",
            icon: <Wifi className="w-12 h-12 mb-4 text-purple-400" />,
            stats: "24/7 Monitoring"
        },
        {
            title: "AI Analytics",
            description: "Machine learning algorithms to predict yields and detect diseases early.",
            icon: <Cpu className="w-12 h-12 mb-4 text-rose-400" />,
            stats: "90% Accuracy"
        },
        {
            title: "Smart Irrigation",
            description: "Automated watering systems that optimize water usage based on real-time data.",
            icon: <Smartphone className="w-12 h-12 mb-4 text-blue-500" />,
            stats: "50% Water Saved"
        }
    ];

    const dailyTips = [
        {
            day: "Today's Top Tip",
            title: "Soil Moisture Management",
            content: "Check soil moisture at root depth, not just the surface. This ensures deep root growth for drought resistance."
        },
        {
            day: "Weekly Focus",
            title: "Traditional Wisdom",
            content: "Observe your local weeds; they can indicate soil conditions. For example, dandelions often grow in calcium-poor soil."
        },
        {
            day: "Tech Tip",
            title: "Update Sensor Firmware",
            content: "Ensure your IoT devices are running the latest firmware to maintain security and data accuracy."
        }
    ];

    return (
        <div className="min-h-screen bg-gray-900 text-white font-sans selection:bg-green-500 selection:text-white">
            {/* Hero Section */}
            <section className="relative h-[60vh] flex items-center justify-center overflow-hidden">
                <div className="absolute inset-0 z-0">
                    <img
                        src="https://images.unsplash.com/photo-1628352081506-83c43123ed6d?auto=format&fit=crop&q=80&w=2000"
                        alt="Modern Farming Background"
                        className="w-full h-full object-cover opacity-40"
                    />
                    <div className="absolute inset-0 bg-gradient-to-b from-gray-900/50 via-gray-900/50 to-gray-900"></div>
                </div>

                <div className="relative z-10 text-center px-4 max-w-4xl mx-auto">
                    <motion.div
                        initial={{ opacity: 0, y: 30 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.8 }}
                    >
                        <span className="inline-block py-1 px-3 rounded-full bg-green-500/20 text-green-400 text-sm font-semibold mb-4 border border-green-500/30 backdrop-blur-sm">
                            Bridging Traditions & Technology
                        </span>
                        <h1 className="text-5xl md:text-7xl font-bold mb-6 bg-clip-text text-transparent bg-gradient-to-r from-green-400 via-emerald-300 to-cyan-400">
                            Farming Practices
                        </h1>
                        <p className="text-xl text-gray-300 mb-8 max-w-2xl mx-auto leading-relaxed">
                            Discover the perfect balance between time-tested traditional wisdom and cutting-edge agricultural technology.
                        </p>
                    </motion.div>
                </div>
            </section>

            {/* Navigation Tabs */}
            <div className="sticky top-0 z-30 bg-gray-900/80 backdrop-blur-md border-b border-gray-800">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="flex justify-center space-x-2 md:space-x-8 overflow-x-auto">
                        {['techniques', 'traditional', 'tools', 'tips'].map((tab) => (
                            <button
                                key={tab}
                                onClick={() => setActiveTab(tab)}
                                className={`py-4 px-2 relative text-sm font-medium transition-colors duration-300 capitalize whitespace-nowrap ${activeTab === tab ? 'text-green-400' : 'text-gray-400 hover:text-gray-200'
                                    }`}
                            >
                                {tab === 'techniques' ? 'Modern Tech' : tab}
                                {activeTab === tab && (
                                    <motion.div
                                        layoutId="activeTab"
                                        className="absolute bottom-0 left-0 right-0 h-0.5 bg-green-400"
                                    />
                                )}
                            </button>
                        ))}
                    </div>
                </div>
            </div>

            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
                <AnimatePresence mode="wait">

                    {/* Techniques Section */}
                    {activeTab === 'techniques' && (
                        <motion.div
                            key="techniques"
                            initial="hidden"
                            animate="visible"
                            exit={{ opacity: 0, y: -20 }}
                            variants={fadeIn}
                            transition={{ duration: 0.5 }}
                            className="space-y-24"
                        >
                            <div className="text-center mb-12">
                                <h2 className="text-3xl font-bold text-white mb-4">Advanced Modern Methods</h2>
                                <p className="text-gray-400">Maximize efficiency with the latest cultivation strategies.</p>
                            </div>

                            {techniques.map((tech, index) => (
                                <motion.div
                                    key={index}
                                    initial={{ opacity: 0, x: index % 2 === 0 ? -50 : 50 }}
                                    whileInView={{ opacity: 1, x: 0 }}
                                    viewport={{ once: true }}
                                    transition={{ duration: 0.6 }}
                                    className={`flex flex-col ${index % 2 === 1 ? 'md:flex-row-reverse' : 'md:flex-row'} items-center gap-12`}
                                >
                                    <div className="w-full md:w-1/2 rounded-2xl overflow-hidden shadow-2xl relative group">
                                        <img
                                            src={tech.image}
                                            alt={tech.title}
                                            className="w-full h-80 object-cover transform transition-transform duration-700 group-hover:scale-110"
                                        />
                                        <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent"></div>
                                    </div>
                                    <div className="w-full md:w-1/2 space-y-6">
                                        <div className="flex items-center space-x-4">
                                            <div className="p-3 bg-gray-800 rounded-lg">{tech.icon}</div>
                                            <h3 className="text-3xl font-bold text-green-300">{tech.title}</h3>
                                        </div>
                                        <p className="text-gray-300 text-lg leading-relaxed">{tech.description}</p>
                                        <ul className="space-y-3">
                                            {tech.benefits.map((benefit, i) => (
                                                <li key={i} className="flex items-center text-gray-400">
                                                    <CheckCircle2 className="w-5 h-5 text-green-500 mr-3" />
                                                    {benefit}
                                                </li>
                                            ))}
                                        </ul>
                                    </div>
                                </motion.div>
                            ))}
                        </motion.div>
                    )}

                    {/* Traditional Methods Section */}
                    {activeTab === 'traditional' && (
                        <motion.div
                            key="traditional"
                            initial="hidden"
                            animate="visible"
                            exit={{ opacity: 0, y: -20 }}
                            variants={fadeIn}
                            transition={{ duration: 0.5 }}
                            className="space-y-24"
                        >
                            <div className="text-center mb-12">
                                <h2 className="text-3xl font-bold text-white mb-4">Time-Tested Traditions</h2>
                                <p className="text-gray-400">Sustainable practices passed down through generations.</p>
                            </div>

                            {traditionalMethods.map((method, index) => (
                                <motion.div
                                    key={index}
                                    initial={{ opacity: 0, x: index % 2 === 0 ? -50 : 50 }}
                                    whileInView={{ opacity: 1, x: 0 }}
                                    viewport={{ once: true }}
                                    transition={{ duration: 0.6 }}
                                    className={`flex flex-col ${index % 2 === 1 ? 'md:flex-row-reverse' : 'md:flex-row'} items-center gap-12`}
                                >
                                    <div className="w-full md:w-1/2 rounded-2xl overflow-hidden shadow-2xl relative group border-4 border-amber-900/30">
                                        <img
                                            src={method.image}
                                            alt={method.title}
                                            className="w-full h-80 object-cover transform transition-transform duration-700 group-hover:scale-110 sepia-[0.3]"
                                        />
                                        <div className="absolute inset-0 bg-gradient-to-t from-amber-900/60 to-transparent"></div>
                                    </div>
                                    <div className="w-full md:w-1/2 space-y-6">
                                        <div className="flex items-center space-x-4">
                                            <div className="p-3 bg-amber-900/40 rounded-lg border border-amber-700/50">{method.icon}</div>
                                            <h3 className="text-3xl font-bold text-amber-200">{method.title}</h3>
                                        </div>
                                        <p className="text-gray-300 text-lg leading-relaxed">{method.description}</p>
                                        <ul className="space-y-3">
                                            {method.benefits.map((benefit, i) => (
                                                <li key={i} className="flex items-center text-amber-100/70">
                                                    <CheckCircle2 className="w-5 h-5 text-amber-500 mr-3" />
                                                    {benefit}
                                                </li>
                                            ))}
                                        </ul>
                                    </div>
                                </motion.div>
                            ))}
                        </motion.div>
                    )}

                    {/* Tools Section */}
                    {activeTab === 'tools' && (
                        <motion.div
                            key="tools"
                            initial="hidden"
                            animate="visible"
                            exit={{ opacity: 0, y: -20 }}
                            variants={fadeIn}
                            className="grid grid-cols-1 md:grid-cols-2 gap-8"
                        >
                            {tools.map((tool, index) => (
                                <motion.div
                                    key={index}
                                    initial={{ opacity: 0, scale: 0.9 }}
                                    whileInView={{ opacity: 1, scale: 1 }}
                                    whileHover={{ y: -10 }}
                                    transition={{ duration: 0.3 }}
                                    viewport={{ once: true }}
                                    className="bg-gray-800/50 backdrop-blur-sm p-8 rounded-2xl border border-gray-700 hover:border-green-500/50 transition-colors group cursor-default"
                                >
                                    <div className="flex justify-between items-start mb-6">
                                        <div className="p-4 bg-gray-700/50 rounded-xl group-hover:bg-gray-700 transition-colors">
                                            {tool.icon}
                                        </div>
                                        <span className="text-4xl font-bold text-gray-700 group-hover:text-green-500/20 transition-colors">0{index + 1}</span>
                                    </div>
                                    <h3 className="text-2xl font-bold text-white mb-3">{tool.title}</h3>
                                    <p className="text-gray-400 mb-6">{tool.description}</p>
                                    <div className="flex items-center text-green-400 font-semibold bg-green-500/10 py-2 px-4 rounded-full w-fit">
                                        <TrendingUp className="w-4 h-4 mr-2" />
                                        {tool.stats}
                                    </div>
                                </motion.div>
                            ))}
                        </motion.div>
                    )}

                    {/* Tips Section */}
                    {activeTab === 'tips' && (
                        <motion.div
                            key="tips"
                            initial="hidden"
                            animate="visible"
                            exit={{ opacity: 0, y: -20 }}
                            variants={fadeIn}
                            className="max-w-3xl mx-auto"
                        >
                            <div className="grid gap-6">
                                {dailyTips.map((tip, index) => (
                                    <motion.div
                                        key={index}
                                        initial={{ opacity: 0, x: -20 }}
                                        whileInView={{ opacity: 1, x: 0 }}
                                        transition={{ delay: index * 0.1 }}
                                        viewport={{ once: true }}
                                        className="bg-gradient-to-r from-gray-800 to-gray-800/50 p-1 rounded-2xl"
                                    >
                                        <div className="bg-gray-900 rounded-xl p-6 h-full border border-gray-700/50">
                                            <div className="flex items-center justify-between mb-4">
                                                <span className="text-xs font-bold tracking-widest text-green-500 uppercase flex items-center">
                                                    <Calendar className="w-3 h-3 mr-1" />
                                                    {tip.day}
                                                </span>
                                                <ArrowRight className="w-5 h-5 text-gray-600" />
                                            </div>
                                            <h3 className="text-xl font-bold text-white mb-2">{tip.title}</h3>
                                            <p className="text-gray-400">{tip.content}</p>
                                        </div>
                                    </motion.div>
                                ))}
                            </div>

                            <div className="mt-12 p-8 bg-green-600 rounded-3xl text-center relative overflow-hidden">
                                <div className="relative z-10">
                                    <h3 className="text-2xl font-bold text-white mb-4">Have a specific question?</h3>
                                    <p className="text-green-100 mb-6">Ask our AI AgriBot for personalized tips tailored to your farm's conditions.</p>
                                    <button className="bg-white text-green-700 font-bold py-3 px-8 rounded-full hover:bg-green-50 transition-colors shadow-lg hover:shadow-xl transform hover:-translate-y-0.5 duration-200">
                                        Ask AgriBot Now
                                    </button>
                                </div>
                                <div className="absolute top-0 right-0 -mt-8 -mr-8 w-32 h-32 bg-green-500 rounded-full opacity-50 blur-2xl"></div>
                                <div className="absolute bottom-0 left-0 -mb-8 -ml-8 w-32 h-32 bg-green-400 rounded-full opacity-50 blur-2xl"></div>
                            </div>
                        </motion.div>
                    )}

                </AnimatePresence>
            </div>
        </div>
    );
};

export default ModernFarming;
