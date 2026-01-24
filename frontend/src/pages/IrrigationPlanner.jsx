import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Droplets, Calendar, Map, Sprout, Check, AlertCircle } from 'lucide-react';

const IrrigationPlanner = () => {
    const [formData, setFormData] = useState({
        cropType: '',
        soilType: '',
        farmSize: '',
        irrigationMethod: ''
    });
    const [schedule, setSchedule] = useState(null);

    const handleCreatePlan = (e) => {
        e.preventDefault();

        // Generate varied schedules based on inputs
        let frequency = "Every 3 Days";
        let duration = "45 Minutes";
        let times = [
            { time: "06:00 AM", action: "Start" },
            { time: "06:45 AM", action: "Stop" }
        ];

        // Crop logic
        if (formData.cropType === 'rice') {
            frequency = "Daily";
            duration = "2 Hours (Flood)";
        } else if (formData.cropType === 'tomato') {
            frequency = "Every 2 Days";
            duration = "30 Minutes (Drip)";
        }

        // Soil logic
        if (formData.soilType === 'sandy') {
            frequency = "Daily (Morning & Evening)";
            duration = "20 Minutes";
            times = [
                { time: "06:00 AM", action: "Start (20 mins)" },
                { time: "06:00 PM", action: "Start (20 mins)" }
            ];
        } else if (formData.soilType === 'clay') {
            frequency = "Every 4 Days";
            duration = "60 Minutes (Split)";
            times = [
                { time: "06:00 AM", action: "Start (30 mins)" },
                { time: "06:30 AM", action: "Pause (Soak)" },
                { time: "07:00 AM", action: "Resume (30 mins)" }
            ];
        }

        setSchedule({
            frequency,
            duration,
            method: formData.irrigationMethod || "Smart AI Recommendation",
            timeline: times
        });
    };

    return (
        <div className="min-h-screen bg-gray-900 text-white font-sans p-6 md:p-12">
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="max-w-6xl mx-auto"
            >
                <div className="text-center mb-12">
                    <h1 className="text-4xl md:text-5xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-cyan-300 mb-4">
                        Smart Irrigation Planner
                    </h1>
                    <p className="text-gray-400 max-w-2xl mx-auto">
                        Optimize your water usage with AI-driven scheduling tailored to your specific crop and soil conditions.
                    </p>
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-2 gap-12">
                    {/* Input Form */}
                    <motion.div
                        initial={{ x: -50, opacity: 0 }}
                        animate={{ x: 0, opacity: 1 }}
                        transition={{ delay: 0.2 }}
                        className="bg-gray-800/50 backdrop-blur-sm p-8 rounded-2xl border border-gray-700 shadow-xl"
                    >
                        <form onSubmit={handleCreatePlan} className="space-y-6">
                            <div>
                                <label className="block text-sm font-medium text-gray-400 mb-2">Crop Type</label>
                                <div className="relative">
                                    <Sprout className="absolute left-3 top-3.5 text-green-500 w-5 h-5" />
                                    <select
                                        className="w-full bg-gray-900 border border-gray-700 rounded-lg py-3 pl-10 pr-4 text-white focus:outline-none focus:border-blue-500 transition-colors"
                                        value={formData.cropType}
                                        onChange={(e) => setFormData({ ...formData, cropType: e.target.value })}
                                        required
                                    >
                                        <option value="">Select a crop...</option>
                                        <option value="wheat">Wheat</option>
                                        <option value="corn">Corn</option>
                                        <option value="rice">Rice</option>
                                        <option value="tomato">Tomato</option>
                                    </select>
                                </div>
                            </div>

                            <div>
                                <label className="block text-sm font-medium text-gray-400 mb-2">Soil Type</label>
                                <div className="relative">
                                    <Map className="absolute left-3 top-3.5 text-yellow-600 w-5 h-5" />
                                    <select
                                        className="w-full bg-gray-900 border border-gray-700 rounded-lg py-3 pl-10 pr-4 text-white focus:outline-none focus:border-blue-500 transition-colors"
                                        value={formData.soilType}
                                        onChange={(e) => setFormData({ ...formData, soilType: e.target.value })}
                                        required
                                    >
                                        <option value="">Select soil type...</option>
                                        <option value="clay">Clay</option>
                                        <option value="sandy">Sandy</option>
                                        <option value="loam">Loam</option>
                                        <option value="silt">Silt</option>
                                    </select>
                                </div>
                            </div>

                            <div className="grid grid-cols-2 gap-6">
                                <div>
                                    <label className="block text-sm font-medium text-gray-400 mb-2">Farm Size (Acres)</label>
                                    <input
                                        type="number"
                                        className="w-full bg-gray-900 border border-gray-700 rounded-lg py-3 px-4 text-white focus:outline-none focus:border-blue-500 transition-colors"
                                        placeholder="e.g. 5"
                                        value={formData.farmSize}
                                        onChange={(e) => setFormData({ ...formData, farmSize: e.target.value })}
                                        required
                                    />
                                </div>
                                <div>
                                    <label className="block text-sm font-medium text-gray-400 mb-2">Method</label>
                                    <select
                                        className="w-full bg-gray-900 border border-gray-700 rounded-lg py-3 px-4 text-white focus:outline-none focus:border-blue-500 transition-colors"
                                        value={formData.irrigationMethod}
                                        onChange={(e) => setFormData({ ...formData, irrigationMethod: e.target.value })}
                                    >
                                        <option value="Drip Irrigation">Drip</option>
                                        <option value="Sprinkler">Sprinkler</option>
                                        <option value="Flood">Flood</option>
                                    </select>
                                </div>
                            </div>

                            <button
                                type="submit"
                                className="w-full bg-gradient-to-r from-blue-600 to-blue-500 hover:from-blue-500 hover:to-blue-400 text-white font-bold py-4 rounded-xl shadow-lg transform transition-all hover:-translate-y-1 hover:shadow-2xl"
                            >
                                Generate Irrigation Plan
                            </button>
                        </form>
                    </motion.div>

                    {/* Results Section */}
                    <motion.div
                        initial={{ x: 50, opacity: 0 }}
                        animate={{ x: 0, opacity: 1 }}
                        transition={{ delay: 0.4 }}
                        className="flex flex-col justify-center"
                    >
                        {schedule ? (
                            <div className="bg-gradient-to-br from-blue-900/50 to-gray-800/50 backdrop-blur-md p-8 rounded-2xl border border-blue-500/30">
                                <div className="flex items-center justify-between mb-8">
                                    <h3 className="text-2xl font-bold text-white flex items-center">
                                        <Calendar className="w-6 h-6 mr-2 text-blue-400" />
                                        Recommended Schedule
                                    </h3>
                                    <span className="bg-blue-500/20 text-blue-300 text-xs font-bold px-3 py-1 rounded-full border border-blue-400/30">
                                        AI OPTIMIZED
                                    </span>
                                </div>

                                <div className="grid grid-cols-2 gap-6 mb-8">
                                    <div className="bg-gray-900/50 p-4 rounded-xl border border-gray-700">
                                        <p className="text-gray-400 text-sm mb-1">Frequency</p>
                                        <p className="text-xl font-bold text-white">{schedule.frequency}</p>
                                    </div>
                                    <div className="bg-gray-900/50 p-4 rounded-xl border border-gray-700">
                                        <p className="text-gray-400 text-sm mb-1">Duration</p>
                                        <p className="text-xl font-bold text-white">{schedule.duration}</p>
                                    </div>
                                </div>

                                <div className="relative border-l-2 border-blue-500/30 ml-3 space-y-8 pl-8 py-2">
                                    {schedule.timeline.map((item, index) => (
                                        <div key={index} className="relative">
                                            <span className="absolute -left-[41px] top-1 w-6 h-6 rounded-full bg-gray-900 border-2 border-blue-500 flex items-center justify-center">
                                                <div className="w-2 h-2 bg-blue-400 rounded-full"></div>
                                            </span>
                                            <p className="text-blue-400 font-bold text-sm">{item.time}</p>
                                            <p className="text-white text-lg">{item.action}</p>
                                        </div>
                                    ))}
                                </div>

                                <div className="mt-8 pt-6 border-t border-gray-700 flex items-start">
                                    <AlertCircle className="w-5 h-5 text-yellow-500 mr-3 flex-shrink-0 mt-0.5" />
                                    <p className="text-gray-400 text-sm">
                                        Based on your clay soil type, we recommend creating intervals to prevent runoff and ensure deep soaking.
                                    </p>
                                </div>
                            </div>
                        ) : (
                            <div className="flex flex-col items-center justify-center h-full text-center border-2 border-dashed border-gray-700 rounded-2xl p-12">
                                <Droplets className="w-20 h-20 text-gray-700 mb-6" />
                                <h3 className="text-xl font-bold text-gray-500">No Plan Generated Yet</h3>
                                <p className="text-gray-600 mt-2">Fill out the farm details to get your optimized irrigation schedule.</p>
                            </div>
                        )}
                    </motion.div>
                </div>
            </motion.div>
        </div>
    );
};

export default IrrigationPlanner;
