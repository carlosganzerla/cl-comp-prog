(defvar *vowels* (list #\a #\e #\i #\o #\u))

(defun is-happy (str)
  (do ((x 0 (1+ x))
       (cont 0))
      ((>= x (length str)) "Sad")
      (if (member (char str x) *vowels*)
          (when (> (incf cont) 2)
            (return "Happy"))
          (setf cont 0))))

(defun main ()
  (dotimes (_ (read))
    (write-string (is-happy (read-line)))
    (terpri)))

(main)
