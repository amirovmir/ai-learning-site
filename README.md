# AI / ML Engineer — Учебник

Интерактивный учебный сайт для разработчиков, которые хотят стать ML/AI-инженерами.

**Сайт:** https://amirovmir.github.io/ai-learning-site/

## Программа

- **Phase 1 — Python + Math + Data:** Python для ML, математика, NumPy/Pandas/SQL, EDA
- **Phase 2 — Classical ML:** основы ML, деревья и ансамбли, unsupervised, валидация и метрики
- **Phase 3 — Deep Learning:** PyTorch, обучение нейросетей, Computer Vision, NLP и трансформеры
- **Phase 4 — LLM & GenAI:** устройство LLM, prompt engineering, RAG, AI-агенты
- **Phase 5 — MLOps & Production:** деплой и мониторинг, ML system design и карьера, фишки и лайфхаки, сравнение моделей

20 разделов · ~270 тем · ссылки для углублённого изучения в каждой теме · тест в конце каждого раздела · прогресс сохраняется в браузере (localStorage).

## Сборка

Контент лежит в `data/section_*.json`, сборка в один самодостаточный `index.html`:

```bash
python build.py
python validate.py   # проверка структуры данных
```
