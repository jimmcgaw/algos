from collections import Counter
import random
import math


def get_probabilities_by_value(values: list[float]):
    return {value: float(count)/len(values)
        for value, count
        in Counter(values).items()
    }


def compute_entropy(values: list[float]):
    return -sum(
        [
            probability * math.log(probability)
            for probability
            in get_probabilities_by_value(values).values()
        ]
    )


def compute_cross_entropy(ground_truth_values: list[float], predicted_values: list[float]):
    gt_probs_by_value = get_probabilities_by_value(ground_truth_values)
    pred_probs_by_value = get_probabilities_by_value(predicted_values)
    # keys in gt but missing from pred
    unique_gt_keys = set(gt_probs_by_value.keys()) - set(pred_probs_by_value.keys())
    # keys in pred but missing from gt
    unique_pred_keys = set(pred_probs_by_value.keys()) - set(gt_probs_by_value.keys())
    # update both dictionarys so we have key symmetry
    pred_probs_by_value.update({gt_key: 0 for gt_key in unique_gt_keys})
    gt_probs_by_value.update({pred_key: 0 for pred_key in unique_pred_keys})
    return -sum(
        [
            gt_probs_by_value[val] * math.log(pred_probs_by_value[val])
            for val
            in gt_probs_by_value.keys()
         ]
    )


print(
    compute_cross_entropy(
        [1,1,1,1],
        [1,2,3,4]
    )
)