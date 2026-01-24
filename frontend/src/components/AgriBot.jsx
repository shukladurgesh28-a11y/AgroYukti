import React, { useState, useRef, useEffect } from 'react';
import { MessageSquare, X, Send, User, Bot, Sparkles } from 'lucide-react';

const AgriBot = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [messages, setMessages] = useState([
        { id: 1, text: "Hello! I'm AgriBot 🤖. How can I help you with your farm today?", sender: 'bot' }
    ]);
    const [inputText, setInputText] = useState("");
    const [isTyping, setIsTyping] = useState(false);
    const messagesEndRef = useRef(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages, isOpen]);

    const handleSendMessage = async (e) => {
        e.preventDefault();
        if (!inputText.trim()) return;

        // Add user message
        const userMessage = { id: Date.now(), text: inputText, sender: 'user' };
        setMessages(prev => [...prev, userMessage]);
        setInputText("");
        setIsTyping(true);

        try {
            const response = await fetch("http://localhost:8000/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    message: userMessage.text
                }),
            });

            const data = await response.json();

            if (data.response) {
                setMessages(prev => [...prev, { id: Date.now() + 1, text: data.response, sender: 'bot' }]);
            } else {
                throw new Error("Invalid response received from server");
            }
        } catch (error) {
            console.error("Error fetching AI response:", error);
            setMessages(prev => [...prev, { id: Date.now() + 1, text: "Sorry, I'm having trouble connecting to the farm network right now. Please try again later.", sender: 'bot' }]);
        } finally {
            setIsTyping(false);
        }
    };

    return (
        <div className="fixed bottom-6 right-6 z-50 font-sans">
            {/* Chat Window */}
            <div
                className={`bg-white rounded-2xl shadow-2xl w-80 sm:w-96 overflow-hidden transition-all duration-300 origin-bottom-right transform ${isOpen ? 'scale-100 opacity-100 mb-4' : 'scale-0 opacity-0 mb-0 h-0'
                    }`}
            >
                {/* Header */}
                <div className="bg-gradient-to-r from-smart-green to-green-600 p-4 flex justify-between items-center text-white">
                    <div className="flex items-center">
                        <div className="bg-white p-1.5 rounded-full mr-3">
                            <Bot size={20} className="text-smart-green" />
                        </div>
                        <div>
                            <h3 className="font-bold">AgriBot Assistant</h3>
                            <div className="flex items-center text-xs text-green-100">
                                <span className="w-2 h-2 bg-green-300 rounded-full mr-1 animate-pulse"></span>
                                Online
                            </div>
                        </div>
                    </div>
                    <button
                        onClick={() => setIsOpen(false)}
                        className="hover:bg-white/20 p-1 rounded-full transition-colors"
                    >
                        <X size={20} />
                    </button>
                </div>

                {/* Messages Area */}
                <div className="h-80 overflow-y-auto p-4 bg-gray-50 flex flex-col space-y-4">
                    {messages.map((msg) => (
                        <div
                            key={msg.id}
                            className={`flex ${msg.sender === 'user' ? 'justify-end' : 'justify-start'}`}
                        >
                            <div
                                className={`max-w-[80%] p-3 rounded-2xl text-sm shadow-sm ${msg.sender === 'user'
                                    ? 'bg-smart-green text-white rounded-tr-none'
                                    : 'bg-white text-gray-800 border border-gray-100 rounded-tl-none'
                                    }`}
                            >
                                {msg.text}
                            </div>
                        </div>
                    ))}
                    {isTyping && (
                        <div className="flex justify-start">
                            <div className="bg-white border border-gray-100 p-3 rounded-2xl rounded-tl-none shadow-sm flex space-x-1">
                                <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></span>
                                <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></span>
                                <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.4s' }}></span>
                            </div>
                        </div>
                    )}
                    <div ref={messagesEndRef} />
                </div>

                {/* Input Area */}
                <form onSubmit={handleSendMessage} className="p-3 bg-white border-t border-gray-100 flex items-center">
                    <input
                        type="text"
                        value={inputText}
                        onChange={(e) => setInputText(e.target.value)}
                        placeholder="Ask anything..."
                        className="flex-1 bg-gray-100 text-gray-800 rounded-full px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-green-200"
                    />
                    <button
                        type="submit"
                        disabled={!inputText.trim()}
                        className="ml-2 p-2 bg-smart-green text-white rounded-full hover:bg-green-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed transform hover:scale-105"
                    >
                        <Send size={18} />
                    </button>
                </form>
            </div>

            {/* Floating Action Button */}
            <button
                onClick={() => setIsOpen(!isOpen)}
                className={`ml-auto w-14 h-14 rounded-full bg-gradient-to-br from-smart-yellow to-yellow-500 shadow-lg flex items-center justify-center text-white hover:scale-110 active:scale-95 transition-all duration-300 ${isOpen ? 'rotate-90 opacity-0 pointer-events-none' : 'rotate-0 opacity-100'
                    }`}
            >
                <MessageSquare size={28} fill="currentColor" />
                <span className="absolute top-0 right-0 w-4 h-4 bg-red-500 rounded-full border-2 border-white"></span>
            </button>

            {/* Close button for FAB state */}
            <button
                onClick={() => setIsOpen(!isOpen)}
                className={`ml-auto w-14 h-14 rounded-full bg-gray-600 shadow-lg flex items-center justify-center text-white hover:bg-gray-700 transition-all duration-300 absolute bottom-0 right-0 ${isOpen ? 'scale-100 opacity-100 rotate-0' : 'scale-0 opacity-0 rotate-90'
                    }`}
            >
                <X size={24} />
            </button>
        </div>
    );
};

export default AgriBot;
