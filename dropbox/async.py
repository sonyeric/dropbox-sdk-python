# Auto-generated by BabelAPI, do not modify.
try:
    from . import babel_validators as bv
except (SystemError, ValueError):
    # Catch errors raised when importing a relative module when not in a package.
    # This makes testing this file directly (outside of a package) easier.
    import babel_validators as bv

class LaunchResultBase(object):
    """
    Result returned by methods that launch an asynchronous job. A method who may
    either launch an asynchronous job, or complete the request synchronously,
    can use this union by extending it, and adding a 'complete' field with the
    type of the synchronous response. See :class:`LaunchEmptyResult` for an
    example.

    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar str async_job_id: This response indicates that the processing is
        asynchronous. The string is an id that can be used to obtain the status
        of the asynchronous job.
    """

    __slots__ = ['_tag', '_value']

    _catch_all = None

    def __init__(self, tag, value=None):
        assert tag in self._tagmap, 'Invalid tag %r.' % tag
        validator = self._tagmap[tag]
        if isinstance(validator, bv.Void):
            assert value is None, 'Void type union member must have None value.'
        elif isinstance(validator, (bv.Struct, bv.Union)):
            validator.validate_type_only(value)
        else:
            validator.validate(value)
        self._tag = tag
        self._value = value

    @classmethod
    def async_job_id(cls, val):
        """
        Create an instance of this class set to the ``async_job_id`` tag with value ``val``.

        :param str val:
        :rtype: LaunchResultBase
        """
        return cls('async_job_id', val)

    def is_async_job_id(self):
        """
        Check if the union tag is ``async_job_id``.

        :rtype: bool
        """
        return self._tag == 'async_job_id'

    def get_async_job_id(self):
        """
        This response indicates that the processing is asynchronous. The string
        is an id that can be used to obtain the status of the asynchronous job.

        Only call this if :meth:`is_async_job_id` is true.

        :rtype: str
        """
        if not self.is_async_job_id():
            raise AttributeError("tag 'async_job_id' not set")
        return self._value

    def __repr__(self):
        return 'LaunchResultBase(%r, %r)' % (self._tag, self._value)

class LaunchEmptyResult(LaunchResultBase):
    """
    Result returned by methods that may either launch an asynchronous job or
    complete synchronously. Upon synchronous completion of the job, no
    additional information is returned.

    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar complete: The job finished synchronously and successfully.
    """

    __slots__ = ['_tag', '_value']

    # Attribute is overwritten below the class definition
    complete = None

    def __init__(self, tag, value=None):
        assert tag in self._tagmap, 'Invalid tag %r.' % tag
        validator = self._tagmap[tag]
        if isinstance(validator, bv.Void):
            assert value is None, 'Void type union member must have None value.'
        elif isinstance(validator, (bv.Struct, bv.Union)):
            validator.validate_type_only(value)
        else:
            validator.validate(value)
        self._tag = tag
        self._value = value

    def is_complete(self):
        """
        Check if the union tag is ``complete``.

        :rtype: bool
        """
        return self._tag == 'complete'

    def __repr__(self):
        return 'LaunchEmptyResult(%r, %r)' % (self._tag, self._value)

class PollArg(object):
    """
    Arguments for methods that poll the status of an asynchronous job.

    :ivar async_job_id: Id of the asynchronous job. This is the value of a
        response returned from the method that launched the job.
    """

    __slots__ = [
        '_async_job_id_value',
        '_async_job_id_present',
    ]

    _has_required_fields = True

    def __init__(self,
                 async_job_id=None):
        self._async_job_id_value = None
        self._async_job_id_present = False
        if async_job_id is not None:
            self.async_job_id = async_job_id

    @property
    def async_job_id(self):
        """
        Id of the asynchronous job. This is the value of a response returned
        from the method that launched the job.

        :rtype: str
        """
        if self._async_job_id_present:
            return self._async_job_id_value
        else:
            raise AttributeError("missing required field 'async_job_id'")

    @async_job_id.setter
    def async_job_id(self, val):
        val = self._async_job_id_validator.validate(val)
        self._async_job_id_value = val
        self._async_job_id_present = True

    @async_job_id.deleter
    def async_job_id(self):
        self._async_job_id_value = None
        self._async_job_id_present = False

    def __repr__(self):
        return 'PollArg(async_job_id={!r})'.format(
            self._async_job_id_value,
        )

class PollResultBase(object):
    """
    Result returned by methods that poll for the status of an asynchronous job.
    Unions that extend this union should add a 'complete' field with a type of
    the information returned upon job completion. See :class:`PollEmptyResult`
    for an example.

    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar in_progress: The asynchronous job is still in progress.
    """

    __slots__ = ['_tag', '_value']

    _catch_all = None
    # Attribute is overwritten below the class definition
    in_progress = None

    def __init__(self, tag, value=None):
        assert tag in self._tagmap, 'Invalid tag %r.' % tag
        validator = self._tagmap[tag]
        if isinstance(validator, bv.Void):
            assert value is None, 'Void type union member must have None value.'
        elif isinstance(validator, (bv.Struct, bv.Union)):
            validator.validate_type_only(value)
        else:
            validator.validate(value)
        self._tag = tag
        self._value = value

    def is_in_progress(self):
        """
        Check if the union tag is ``in_progress``.

        :rtype: bool
        """
        return self._tag == 'in_progress'

    def __repr__(self):
        return 'PollResultBase(%r, %r)' % (self._tag, self._value)

class PollEmptyResult(PollResultBase):
    """
    Result returned by methods that poll for the status of an asynchronous job.
    Upon completion of the job, no additional information is returned.

    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar complete: The asynchronous job has completed successfully.
    """

    __slots__ = ['_tag', '_value']

    # Attribute is overwritten below the class definition
    complete = None

    def __init__(self, tag, value=None):
        assert tag in self._tagmap, 'Invalid tag %r.' % tag
        validator = self._tagmap[tag]
        if isinstance(validator, bv.Void):
            assert value is None, 'Void type union member must have None value.'
        elif isinstance(validator, (bv.Struct, bv.Union)):
            validator.validate_type_only(value)
        else:
            validator.validate(value)
        self._tag = tag
        self._value = value

    def is_complete(self):
        """
        Check if the union tag is ``complete``.

        :rtype: bool
        """
        return self._tag == 'complete'

    def __repr__(self):
        return 'PollEmptyResult(%r, %r)' % (self._tag, self._value)

class PollError(object):
    """
    Error returned by methods for polling the status of asynchronous job.

    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar invalid_async_job_id: The job ID is invalid.
    :ivar internal_error: Something went wrong with the job on Dropbox's end.
        You'll need to verify that the action you were taking succeeded, and if
        not, try again. This should happen very rarely.
    :ivar other: An unspecified error.
    """

    __slots__ = ['_tag', '_value']

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    invalid_async_job_id = None
    # Attribute is overwritten below the class definition
    internal_error = None
    # Attribute is overwritten below the class definition
    other = None

    def __init__(self, tag, value=None):
        assert tag in self._tagmap, 'Invalid tag %r.' % tag
        validator = self._tagmap[tag]
        if isinstance(validator, bv.Void):
            assert value is None, 'Void type union member must have None value.'
        elif isinstance(validator, (bv.Struct, bv.Union)):
            validator.validate_type_only(value)
        else:
            validator.validate(value)
        self._tag = tag
        self._value = value

    def is_invalid_async_job_id(self):
        """
        Check if the union tag is ``invalid_async_job_id``.

        :rtype: bool
        """
        return self._tag == 'invalid_async_job_id'

    def is_internal_error(self):
        """
        Check if the union tag is ``internal_error``.

        :rtype: bool
        """
        return self._tag == 'internal_error'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def __repr__(self):
        return 'PollError(%r, %r)' % (self._tag, self._value)

LaunchResultBase._async_job_id_validator = bv.String(min_length=1)
LaunchResultBase._tagmap = {
    'async_job_id': LaunchResultBase._async_job_id_validator,
}

LaunchEmptyResult._complete_validator = bv.Void()
LaunchEmptyResult._tagmap = {
    'complete': LaunchEmptyResult._complete_validator,
}
LaunchEmptyResult._tagmap.update(LaunchResultBase._tagmap)

LaunchEmptyResult.complete = LaunchEmptyResult('complete')

PollArg._async_job_id_validator = bv.String(min_length=1)
PollArg._all_field_names_ = set(['async_job_id'])
PollArg._all_fields_ = [('async_job_id', PollArg._async_job_id_validator)]

PollResultBase._in_progress_validator = bv.Void()
PollResultBase._tagmap = {
    'in_progress': PollResultBase._in_progress_validator,
}

PollResultBase.in_progress = PollResultBase('in_progress')

PollEmptyResult._complete_validator = bv.Void()
PollEmptyResult._tagmap = {
    'complete': PollEmptyResult._complete_validator,
}
PollEmptyResult._tagmap.update(PollResultBase._tagmap)

PollEmptyResult.complete = PollEmptyResult('complete')

PollError._invalid_async_job_id_validator = bv.Void()
PollError._internal_error_validator = bv.Void()
PollError._other_validator = bv.Void()
PollError._tagmap = {
    'invalid_async_job_id': PollError._invalid_async_job_id_validator,
    'internal_error': PollError._internal_error_validator,
    'other': PollError._other_validator,
}

PollError.invalid_async_job_id = PollError('invalid_async_job_id')
PollError.internal_error = PollError('internal_error')
PollError.other = PollError('other')
