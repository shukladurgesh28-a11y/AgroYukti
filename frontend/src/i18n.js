import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import LanguageDetector from 'i18next-browser-languagedetector';

import en from './locales/en.json';
import hi from './locales/hi.json';
import bn from './locales/bn.json';
import te from './locales/te.json';
import mr from './locales/mr.json';
import ta from './locales/ta.json';
import ur from './locales/ur.json';
import gu from './locales/gu.json';
import kn from './locales/kn.json';
import ml from './locales/ml.json';
import pa from './locales/pa.json';
import or from './locales/or.json';
import as from './locales/as.json';

i18n
    .use(LanguageDetector)
    .use(initReactI18next)
    .init({
        resources: {
            en: { translation: en },
            hi: { translation: hi },
            bn: { translation: bn },
            te: { translation: te },
            mr: { translation: mr },
            ta: { translation: ta },
            ur: { translation: ur },
            gu: { translation: gu },
            kn: { translation: kn },
            ml: { translation: ml },
            pa: { translation: pa },
            or: { translation: or },
            as: { translation: as },
        },
        fallbackLng: 'en',
        interpolation: {
            escapeValue: false,
        },
        supportedLngs: ['en', 'hi', 'bn', 'te', 'mr', 'ta', 'ur', 'gu', 'kn', 'ml', 'pa', 'or', 'as'],
    });

export default i18n;
