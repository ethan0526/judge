from dmoj.result import CheckerResult

verdict = u"\u2717\u2713"

def check(process_output, judge_output, point_value, feedback=False, **kwargs):
    process_lines = filter(None, process_output.strip().split("\n"))
    judge_lines = filter(None, judge_output.strip().split("\n"))

    cases = [verdict[0]] * len(judge_lines)
    count = 0

    for i, (process_line, judge_line) in enumerate(zip(process_lines, judge_lines)):
        if process_line == judge_line:
            cases[i] = verdict[1]
            count += 1

    if not count or len(process_lines) > len(judge_lines):
        return CheckerResult(False, 0)
    return CheckerResult(True, point_value * (1.0 * count / len(judge_lines)), ''.join(cases) if feedback else "")
