def mlDecorator(ml_methods, metrics):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("=== Machine Learning Decorator ===")
            for ml_method in ml_methods:
                print(f"Applying {ml_method}...")

            for metric in metrics:
                print(f"Calculating {metric}...")

            result = func(*args, **kwargs)
            print("===============================")
            return result

        return wrapper
    return decorator
