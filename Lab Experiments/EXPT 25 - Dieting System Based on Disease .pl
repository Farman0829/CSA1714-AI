% Diet Suggestion System Based on Disease

% Disease facts
disease(diabetes).
disease(obesity).
disease(anemia).
disease(high_bp).

% Diet suggestions
diet(diabetes, 'Low sugar and high fibre foods').
diet(obesity, 'Low calorie foods and vegetables').
diet(anemia, 'Iron rich foods like spinach and beans').
diet(high_bp, 'Low salt foods and fruits').

% Rule to suggest diet based on disease
suggest_diet(Disease, Diet) :-
    disease(Disease),
    diet(Disease, Diet).