import React, { useState, useEffect } from 'react';

const AgriNewsSection = () => {
  const articles = [
    {
      id: 1,
      image: "https://pmkisan.gov.in/images/PMKISAN_Logo_New.png",
      date: "Govt Scheme",
      author: "Ministry of Agriculture",
      comments: "Active",
      title: "Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)",
      description: "Financial support of ₹6,000 per year for farmer families. Direct bank transfer in three equal installments.",
      applyLink: "https://pmkisan.gov.in/"
    },
    {
      id: 2,
      image: "https://soilhealth.dac.gov.in/Content/images/soil_health_card_logo.png",
      date: "Govt Scheme",
      author: "Dept of Agriculture",
      comments: "Active",
      title: "Soil Health Card Scheme (SHC)",
      description: "Get a Soil Health Card to know your soil's nutrient status and receive fertilizer recommendations for better yield.",
      applyLink: "https://soilhealth.dac.gov.in/"
    },
    {
      id: 3,
      image: "https://pmfby.gov.in/assets/img/PMFBY.png",
      date: "Insurance",
      author: "GOI",
      comments: "Active",
      title: "Pradhan Mantri Fasal Bima Yojana (PMFBY)",
      description: "Comprehensive crop insurance to protect against non-preventable natural risks from pre-sowing to post-harvest.",
      applyLink: "https://pmfby.gov.in/"
    }
  ];

  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      const element = document.getElementById('news-section');
      if (element) {
        const position = element.getBoundingClientRect();
        if (position.top < window.innerHeight * 0.75) {
          setIsVisible(true);
        }
      }
    };

    handleScroll();

    window.addEventListener('scroll', handleScroll);

    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  return (
    <div id="news-section" className="relative py-16 bg-smart-green">
      <div className="max-w-6xl mx-auto px-4">
        <div className={`text-center mb-12 transition-all duration-1000 ${isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'}`}>
          <h3 className="text-smart-yellow font-semibold mb-2 tracking-wider uppercase">
            FROM THE BLOG
          </h3>
          <h2 className="text-4xl font-bold text-white mb-4 relative inline-block">
            Schemes & Latest News
            <span className="absolute -bottom-2 left-0 h-1 w-full bg-smart-yellow"></span>
          </h2>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {articles.map((article, index) => (
            <div
              key={article.id}
              className={`bg-white rounded-lg overflow-hidden shadow-lg transition-all duration-700 transform ${isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'}`}
              style={{ transitionDelay: `${index * 200}ms` }}
            >
              <div className="relative overflow-hidden h-56">
                <img
                  src={article.image}
                  alt={article.title}
                  className="w-full h-full object-contain p-4 bg-gray-50 transition-transform duration-500 hover:scale-105"
                />
                <div className="absolute bottom-4 left-4">
                  <div className="bg-smart-yellow text-smart-green px-3 py-1 text-sm font-medium rounded">
                    {article.date}
                  </div>
                </div>
              </div>

              <div className="p-6 bg-white">
                <div className="flex items-center justify-between text-sm text-gray-500 mb-4">
                  <div className="flex items-center space-x-1">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-smart-yellow" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                    </svg>
                    <span className="text-gray-400">{article.author}</span>
                  </div>
                  <div className="flex items-center space-x-1">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-smart-yellow" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                    </svg>
                    <span className={`text-xs font-bold px-2 py-0.5 rounded ${article.comments === 'Active' ? 'bg-green-100 text-green-600' : 'bg-gray-100'}`}>
                      {article.comments}
                    </span>
                  </div>
                </div>

                <h3 className="text-xl font-bold mb-3 text-gray-800 hover:text-smart-yellow transition-colors duration-300">
                </h3>

                <p className="text-gray-600 text-sm mb-4 line-clamp-3">
                  {article.description}
                </p>

                {article.applyLink && (
                  <a
                    href={article.applyLink}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-block bg-smart-green text-white px-4 py-2 rounded text-sm font-medium hover:bg-green-700 transition"
                  >
                    Apply Now →
                  </a>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default AgriNewsSection;