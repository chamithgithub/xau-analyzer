# decision_engine.py

def determine_final_signal(articles):
    """
    Given a list of analyzed articles (each with 'impact'), return:
    - final signal: UP / DOWN / NORMAL
    - summary reason
    - count breakdown
    """
    bullish = sum(1 for a in articles if a['impact'] == 'bullish')
    bearish = sum(1 for a in articles if a['impact'] == 'bearish')
    neutral = sum(1 for a in articles if a['impact'] == 'neutral')

    if bullish > bearish:
        signal = "UP"
        reason = f"{bullish} bullish vs {bearish} bearish articles detected."
    elif bearish > bullish:
        signal = "DOWN"
        reason = f"{bearish} bearish vs {bullish} bullish articles detected."
    else:
        signal = "NORMAL"
        reason = f"Balanced or low-impact news ({bullish} bullish, {bearish} bearish, {neutral} neutral)."

    return {
        "signal": signal,
        "reason": reason,
        "bullish": bullish,
        "bearish": bearish,
        "neutral": neutral
    }
