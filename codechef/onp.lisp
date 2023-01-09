(defun parse (in out)
  (do ((chr (read-char in t nil) (read-char in t nil))
       (op-stack nil))
      ((or (eql chr t) (eql chr #\Newline)))
      (cond
        ((char= #\) chr) (write-char (pop op-stack) out))
        ((>= 122 (char-code chr) 97) (write-char chr out))
        ((not (char= #\( chr)) (push chr op-stack)))))

(defun main ()
  (dotimes (_ (read))
    (parse *standard-input* *standard-output*)
    (terpri)))

(main)
