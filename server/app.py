from flask import abort, jsonify, Flask, request
import gpt_2_simple as gpt2

app = Flask("ghostwriter")

model_name = "124M"


@app.route('/ideas')
def generate_ideas():
    prefix = request.args.get("prefix")
    length = int(request.args.get("length", 50))
    samples = int(request.args.get("samples", 1))

    if samples <= 0 or samples > 5:
        abort(
            jsonify(
                {"message": "Samples value is invalid, min 1 and max 5 allowed."},
                400,
            )
        )

    session = gpt2.start_tf_sess()
    gpt2.load_gpt2(session, model_name=model_name)

    ideas = gpt2.generate(
        session,
        model_name=model_name,
        prefix=prefix,
        length=length,
        nsamples=samples,
        batch_size=samples,
    )

    session.close()

    return jsonify(ideas=ideas)
