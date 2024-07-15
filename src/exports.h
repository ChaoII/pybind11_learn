
#ifndef WHEELBIND_EXPORT_H
#define WHEELBIND_EXPORT_H

#ifdef WHEELBIND_STATIC_DEFINE
#  define WHEELBIND_EXPORT
#  define WHEELBIND_NO_EXPORT
#else
#  ifndef WHEELBIND_EXPORT
#    ifdef wheelbind_EXPORTS
        /* We are building this library */
#      define WHEELBIND_EXPORT __attribute__((visibility("default")))
#    else
        /* We are using this library */
#      define WHEELBIND_EXPORT __attribute__((visibility("default")))
#    endif
#  endif

#  ifndef WHEELBIND_NO_EXPORT
#    define WHEELBIND_NO_EXPORT __attribute__((visibility("hidden")))
#  endif
#endif

#ifndef WHEELBIND_DEPRECATED
#  define WHEELBIND_DEPRECATED __attribute__ ((__deprecated__))
#endif

#ifndef WHEELBIND_DEPRECATED_EXPORT
#  define WHEELBIND_DEPRECATED_EXPORT WHEELBIND_EXPORT WHEELBIND_DEPRECATED
#endif

#ifndef WHEELBIND_DEPRECATED_NO_EXPORT
#  define WHEELBIND_DEPRECATED_NO_EXPORT WHEELBIND_NO_EXPORT WHEELBIND_DEPRECATED
#endif

#if 0 /* DEFINE_NO_DEPRECATED */
#  ifndef WHEELBIND_NO_DEPRECATED
#    define WHEELBIND_NO_DEPRECATED
#  endif
#endif

#endif /* WHEELBIND_EXPORT_H */
