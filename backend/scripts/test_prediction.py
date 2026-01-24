import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from scripts.predict_with_graph import get_price_predictions

print("Running prediction test...")
try:
    results = get_price_predictions()
    print(f"Successfully generated predictions for {len(results)} crops.")
    
    # Check for specific fruits
    fruits = [r for r in results if r['crop'] in ['apple', 'papaya', 'mango']]
    print(f"Found {len(fruits)} target fruits.")
    
    if len(fruits) > 0:
        print("Sample fruit data:", fruits[0]['crop'], fruits[0]['predictions'][0])
        
    # Check for errors
    errors = [r for r in results if 'error' in r]
    if errors:
        print(f"Encountered {len(errors)} errors:")
        for e in errors:
            print(f"- {e['crop']}: {e['error']}")
            
except Exception as e:
    print(f"Test failed with error: {e}")
