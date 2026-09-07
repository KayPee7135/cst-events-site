import json
from datetime import date
from html import escape
from pathlib import Path
from string import Template


def load_events(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return data["events"]


def upcoming(events, today):
    future = [e for e in events if e["date"] >= today]
    return sorted(future, key=lambda e: e["date"])


def render(events):
    cards = []
    for index, event in enumerate(events):
        day = date.fromisoformat(event["date"])
        cards.append(
            '<li class="event-card">'
            '<div class="card-top">'
            f'<time class="date-block" datetime="{day.isoformat()}">'
            f'<span class="month">{day.strftime("%b")}</span>'
            f'<span class="day">{day.day:02d}</span></time>'
            f'<span class="event-number" aria-hidden="true">/{index + 1:02d}</span>'
            '</div>'
            f'<h3>{escape(event["title"])}</h3>'
            '<div class="card-meta">'
            f'<span>{day.strftime("%A")} <span aria-hidden="true">&middot;</span> {day.year}</span>'
            f'<span class="venue"><span aria-hidden="true">&#9678;</span> {escape(event["venue"])}</span>'
            '</div></li>'
        )
    content = '<ul class="events-grid">' + "\n".join(cards) + '</ul>' if cards else (
        '<div class="empty-state"><h3>A little breather.</h3>'
        '<p>No upcoming events right now. Check back for the next club gathering.</p></div>'
    )
    template = Template(Path(__file__).with_name("site_template.html").read_text(encoding="utf-8"))
    return template.substitute(
        event_content=content,
        event_count=f'{len(events):02d}',
        count_label="event ahead" if len(events) == 1 else "events ahead",
    )


def main():
    events = upcoming(load_events("events.json"), date.today().isoformat())
    Path("dist").mkdir(exist_ok=True)
    Path("dist/index.html").write_text(render(events), encoding="utf-8")
    Path("dist/styles.css").write_text(
        Path(__file__).with_name("styles.css").read_text(encoding="utf-8"), encoding="utf-8"
    )
    print(f"wrote dist/index.html with {len(events)} events")


if __name__ == "__main__":
    main()
