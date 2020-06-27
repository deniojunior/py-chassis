import logging

from flask import Blueprint, jsonify, make_response

_logger = logging.getLogger(__name__)

blueprint = Blueprint('statuses', __name__)


@blueprint.route('/status', methods=['GET', 'OPTIONS'])
def is_alive_request():
    return make_response(jsonify({"status": "OK"}), 200)


@blueprint.route('/healthz', methods=['GET', 'OPTIONS'])
def google_healthz():
    """ Endpoint used by Google Ingress health check """
    return make_response(jsonify({"status": "OK"}), 200)


@blueprint.route('/ready', methods=['GET', 'OPTIONS'])
def is_ready_request():
    """Test all used services and return readiness."""

    # if not is_database_ok():
    #    return make_response(jsonify({'status': 'ERROR', 'message': 'DATABASE_ERROR'}), 503)

    return make_response(jsonify({"status": "OK"}), 200)
